from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['User_Info']

def create_document(collection_name, data):
    collection = db[collection_name]
    return collection.insert_one(data).inserted_id

def read_documents(collection_name, query=None):
    collection = db[collection_name]
    return collection.find(query)

def update_document(collection_name, query, update):
    collection = db[collection_name]
    return collection.update_one(query, update).modified_count

def delete_document(collection_name, query):
    collection = db[collection_name]
    return collection.delete_one(query).deleted_count