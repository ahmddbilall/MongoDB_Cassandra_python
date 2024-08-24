from cassandra.cluster import Cluster
import uuid

class cassandra:
    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect()

    def create_keyspace(self):
        query = """
        CREATE KEYSPACE IF NOT EXISTS test_keyspace
        WITH REPLICATION = {
            'class': 'SimpleStrategy',
            'replication_factor': 2
        }
        """
        try:
            self.session.execute(query)
            return True  # Keyspace creation is successful or already exists
        except Exception as e:
            print(f"Error creating keyspace: {e}")
            return False  # Return False if an error occurs


    def create_table(self):
        self.session.execute("""
        CREATE TABLE IF NOT EXISTS test_keyspace.test_table (
            id UUID PRIMARY KEY,
            name text,
            email TEXT,
            phone TEXT,
            address TEXT,
            age INT,
            image BLOB,
            pdf BLOB
        )
        """)

    def insert_data(self, name, email, phone, address, age, image=None, pdf=None):
        id = uuid.uuid4()  
        query = """
        INSERT INTO test_keyspace.test_table (id, name, email, phone, address, age, image, pdf)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        image_blob = bytearray(image) if image else None
        pdf_blob = bytearray(pdf) if pdf else None
        try:
            self.session.execute(query, (id, name, email, phone, address, age, image_blob, pdf_blob))
            return True
        except Exception as e:
            print(f"\n\nError inserting data: {e}")
            return False

    def select_data(self):
        rows = self.session.execute("SELECT * FROM test_keyspace.test_table")
        return rows

    def select_data_by_id(self, id):
        query = "SELECT * FROM test_keyspace.test_table WHERE id=%s"
        rows = self.session.execute(query, (id,))
        return rows

    def update_data(self, id, name, email, phone, address, age, image=None, pdf=None):
        query = """
        UPDATE test_keyspace.test_table 
        SET name=%s, email=%s, phone=%s, address=%s, age=%s, image=%s, pdf=%s
        WHERE id=%s
        """
        image_blob = bytearray(image) if image else None
        pdf_blob = bytearray(pdf) if pdf else None
        try:
            self.session.execute(query, (name, email, phone, address, age, image_blob, pdf_blob, id))
            return True
        except Exception as e:
            print(f"\n\nError updating data: {e}")
            return False
        

    def delete_data(self, id):
        query = "DELETE FROM test_keyspace.test_table WHERE id=%s"
        try:
            self.session.execute(query, (id,))
            return True
        except Exception as e:
            print(f"\n\nError deleting data: {e}")
            return False


    def close_connection(self):
        self.cluster.shutdown()

    def delete_table(self):
        self.session.execute("DROP TABLE IF EXISTS test_keyspace.test_table")

    def truncate_table(self):
        self.session.execute("TRUNCATE test_keyspace.test_table")

    def delete_keyspace(self):
        self.session.execute("DROP KEYSPACE IF EXISTS test_keyspace")
