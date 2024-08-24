import streamlit as st

def main():
    st.title('Welcome to the Streamlit App!')

    st.markdown("""
    ## Introduction
    Welcome to the home page of our Streamlit application!

    This app provides a simple interface to interact with NoSQL databases, including **Cassandra** and **MongoDB**. 

    ### What You Can Do:
    - **Perform CRUD operations** (Create, Read, Update, Delete) on records.
    - **View records** stored in the databases.
    - **Insert new records** into the databases.
    - **Update existing records**.
    - **Delete records** when needed.
    
    ### How to Use:
    1. **Select the database** you want to work with from the sidebar.
    2. **Choose the operation** you want to perform from the available options.
    3. **Follow the prompts** to interact with the database.

    Explore the features and get started with managing your data efficiently!
    """)

    st.markdown("""
    ### Features
    - **Cassandra**: A highly scalable and distributed NoSQL database.
    - **MongoDB**: A flexible, document-oriented NoSQL database.

    ### Contact
    If you have any questions or feedback, feel free to reach out!

    Happy data managing!
    """)

if __name__ == "__main__":
    main()
