from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create or switch to a database
db = client['example_db']

# Create or switch to a collection
collection = db['example_collection']

# Insert a document
document = {'name': 'John Doe', 'age': 29, 'city': 'New York'}
collection.insert_one(document)

# Query the document
result = collection.find_one({'name': 'John Doe'})
print("Inserted Document:", result)

# Update the document
collection.update_one({'name': 'John Doe'}, {'': {'age': 30}})

# Query the updated document
updated_result = collection.find_one({'name': 'John Doe'})
print("Updated Document:", updated_result)

# Delete the document
collection.delete_one({'name': 'John Doe'})

# Verify deletion
deleted_result = collection.find_one({'name': 'John Doe'})
print("Deleted Document:", deleted_result)

