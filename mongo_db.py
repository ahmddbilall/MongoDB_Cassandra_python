from pymongo import MongoClient
import uuid

class MongoDB:
    def __init__(self, db_name='test_db', collection_name='test_collection'):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_data(self, name, email, phone, address, age, image=None, pdf=None):
        # Generate a new UUID
        doc_id = str(uuid.uuid4())
        document = {
            '_id': doc_id,  # Use the generated UUID as the document _id
            'name': name,
            'email': email,
            'phone': phone,
            'address': address,
            'age': age,
            'image': image,
            'pdf': pdf
        }
        try:
            result = self.collection.insert_one(document)
            return result.inserted_id  # Return the inserted ID
        except Exception as e:
            print(f"\n\nError inserting data: {e}")


            return None

    def select_data(self):
        # Return the data with '_id' field included
        return self.collection.find({}, {'_id': 1, 'name': 1, 'email': 1, 'phone': 1, 'address': 1, 'age': 1, 'image': 1, 'pdf': 1})


    # def select_data(self):
    #     return self.collection.find()

    def select_data_by_id(self, doc_id):
        try:
            return self.collection.find_one({'_id': doc_id})
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None

    def update_data(self, doc_id, name=None, email=None, phone=None, address=None, age=None, image=None, pdf=None):
        try:
            update_fields = {}
            if name is not None:
                update_fields['name'] = name
            if email is not None:
                update_fields['email'] = email
            if phone is not None:
                update_fields['phone'] = phone
            if address is not None:
                update_fields['address'] = address
            if age is not None:
                update_fields['age'] = age
            if image is not None:
                update_fields['image'] = image
            if pdf is not None:
                update_fields['pdf'] = pdf

            result = self.collection.update_one({'_id': doc_id}, {'$set': update_fields})
            return result.modified_count > 0
        except Exception as e:
            print(f"\n\nError updating data: {e}")
            return False

    def delete_data(self, doc_id):
        try:
            result = self.collection.delete_one({'_id': doc_id})
            return result.deleted_count > 0
        except Exception as e:
            print(f"\n\nError deleting data: {e}")
            return False

    def close_connection(self):
        self.client.close()

    def drop_collection(self):
        self.collection.drop()

    def drop_database(self):
        self.client.drop_database(self.db.name)
