import streamlit as st
from mongo_db import MongoDB
import io

db = MongoDB()

def main():
    st.title("MongoDB Database Operations")

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
    documents = db.select_data()

    if documents:
        for index, doc in enumerate(documents):
            doc_dict = {k: v for k, v in doc.items() if k != '_id'}
            col1, col2 = st.columns([2, 1])

            with col1:
                if doc.get('image'):
                    st.image(io.BytesIO(doc['image']), caption='Uploaded Image', use_column_width=True)
                else:
                    st.write("No image available.")
                
                if doc.get('pdf'):
                    pdf_data = io.BytesIO(doc['pdf'])
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
                st.markdown(f"**ID:** {doc['_id']}")
                for key, value in doc_dict.items():
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
                inserted_id = db.insert_data(name, email, phone, address, age, image_blob, pdf_blob)
                if inserted_id:
                    st.success(f"Record inserted successfully! ID: {inserted_id}")
                else:
                    st.error("Error inserting record.")

def update_record():
    doc_id = st.text_input("Record ID (ObjectId)", "")
    if doc_id:
        record = db.select_data_by_id(doc_id)
        if record:
            with st.form(key='update_form'):
                name = st.text_input("Name", record.get('name', ''))
                email = st.text_input("Email", record.get('email', ''))
                phone = st.text_input("Phone", record.get('phone', ''))
                address = st.text_input("Address", record.get('address', ''))
                age = st.number_input("Age", min_value=0, value=record.get('age', 0))
                image = st.file_uploader("Upload New Image", type=["jpg", "png"])
                pdf = st.file_uploader("Upload New PDF", type=["pdf"])

                submit_button = st.form_submit_button("Update Record")

                if submit_button:
                    image_blob = image.read() if image else record.get('image')
                    pdf_blob = pdf.read() if pdf else record.get('pdf')
                    if db.update_data(doc_id, name, email, phone, address, age, image_blob, pdf_blob):
                        st.success("Record updated successfully!")
                    else:
                        st.error("Error updating record.")
        else:
            st.error("Record not found.")

def delete_record():
    doc_id = st.text_input("Record ID (ObjectId)", "")
    if doc_id:
        if st.button("Delete Record"):
            if db.delete_data(doc_id):
                st.success("Record deleted successfully!")
            else:
                st.error("Error deleting record.")

if __name__ == "__main__":
    main()
