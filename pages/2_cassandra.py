import streamlit as st
from cassandra_db import cassandra  
import uuid
import io

db = cassandra()
db.create_keyspace()
db.create_table()

def main():
    st.title("Cassandra Database Operations")

    menu = ["View All", "Insert", "Update", "Delete"]
    choice = st.sidebar.selectbox("Select Operation", menu)

    if choice == "View All":
        st.subheader("View All Records")
        view_all_records()

    elif choice == "Insert":
        st.subheader("Insert New Record")
        insert_record()

    elif choice == "Update":
        st.subheader("Update Record")
        update_record()

    elif choice == "Delete":
        st.subheader("Delete Record")

        delete_record()


def view_all_records():
    rows = db.select_data()
 
    if rows:
        for index, row in enumerate(rows):
            row_dict = {k: (str(v) if isinstance(v, uuid.UUID) else v) for k, v in row._asdict().items()}

            col1, col2 = st.columns([2, 1])  
            
            with col1:
                if row_dict.get('image'):
                    st.image(io.BytesIO(row_dict['image']), caption='Uploaded Image', use_column_width=True)
                else:
                    st.write("No image available.")
                
                if row_dict.get('pdf'):
                    pdf_data = io.BytesIO(row_dict['pdf'])
                    st.download_button(
                        label="Download PDF",
                        data=pdf_data,
                        file_name='document.pdf',
                        mime='application/pdf',
                        key=f'download_button_{index}'
                    )
                else:
                    st.write("No PDF available.")
            
            with col2:
                st.markdown("**Record Details:**")
                for key, value in row_dict.items():
                    if key not in ['image', 'pdf']:
                        st.markdown(f"**{key}:** {value}")
            
            st.write("\n\n---\n\n")  

    else:
        st.write("No records found.")


def insert_record():
    with st.form(key='insert_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        address = st.text_input("Address")
        age = st.number_input("Age", min_value=0)
        image = st.file_uploader("Upload Image", type=["jpg", "png"])
        pdf = st.file_uploader("Upload PDF", type=["pdf"])

        submit_button = st.form_submit_button("Insert Record")

        if submit_button:
            if (not name) or (not email) or (not phone) or (not address) or (not age):
                st.error("Please fill all the fields.")
            else:
                image_blob = image.read() if image else None
                pdf_blob = pdf.read() if pdf else None
                if db.insert_data(name, email, phone, address, age, image_blob, pdf_blob):
                    st.success("Record inserted successfully!")
                else:
                    st.error("Error inserting record.")


def update_record():
    id = st.text_input("Record ID (UUID)", "")
    if id:
        try:
            id = uuid.UUID(id)
            record = db.select_data_by_id(id)
            if record:
                record = list(record)[0]
                with st.form(key='update_form'):
                    name = st.text_input("Name", record.name)
                    email = st.text_input("Email", record.email)
                    phone = st.text_input("Phone", record.phone)
                    address = st.text_input("Address", record.address)
                    age = st.number_input("Age", min_value=0, value=record.age)
                    image = st.file_uploader("Upload New Image", type=["jpg", "png"])
                    pdf = st.file_uploader("Upload New PDF", type=["pdf"])

                    submit_button = st.form_submit_button("Update Record")

                    if submit_button:

                        image_blob = image.read() if image else record.image
                        pdf_blob = pdf.read() if pdf else record.pdf
                        if db.update_data(id, name, email, phone, address, age, image_blob, pdf_blob):
                            st.success("Record updated successfully!")
                        else:
                            st.error("Error updating record.")
            else:
                st.error("Record not found.")
        except ValueError:
            st.error("Invalid UUID format.")


def delete_record():
    id = st.text_input("Record ID (UUID)", "")
    if id:
        try:
            id = uuid.UUID(id)
            if st.button("Delete Record"):

                if db.delete_data(id):
                    st.success("Record deleted successfully!")
                else:
                    st.error("Error deleting record.")
        except ValueError:
            st.error("Invalid UUID format.")

if __name__ == "__main__":
    main()

