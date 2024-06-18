NoSQL, or "Not Only SQL," refers to a category of database management systems that differ from traditional relational databases (SQL databases) in several key ways. Here’s an explanation with examples:

### Characteristics of NoSQL Databases:

1. **Non-relational Structure**: NoSQL databases do not adhere to the tabular structure of relational databases. They use different data models suited for specific types of data and applications.

2. **Scalability**: NoSQL databases are designed to scale out horizontally, meaning they can handle large amounts of data across multiple servers or clusters. This is in contrast to relational databases, which often scale vertically (upgrading hardware) and can become slower with increased data volume.

3. **Flexible Schema**: Unlike relational databases that enforce a rigid schema (structure of the data), NoSQL databases offer more flexibility. They can store data in various formats like key-value pairs, document-oriented, column-oriented, or graph databases.

4. **Specialized Use Cases**: NoSQL databases are particularly suitable for applications with large-scale data requirements, such as social networks (Facebook), e-commerce platforms (Amazon), and search engines (Google). These applications demand high performance and scalability, which NoSQL databases provide efficiently.

### Examples of NoSQL Databases:

1. **MongoDB**: A document-oriented NoSQL database that stores data in JSON-like documents. It's widely used for its scalability and flexibility, particularly in content management systems, real-time analytics, and mobile applications.

2. **Redis**: A key-value store that keeps data in-memory, making it extremely fast and suitable for caching, session management, and real-time analytics.

3. **Cassandra**: A column-oriented NoSQL database designed for handling large amounts of data across many commodity servers. It's used in applications needing high availability and scalability, such as IoT (Internet of Things) and time-series data.

### Advantages of NoSQL Databases:

- **Scalability**: NoSQL databases can easily scale horizontally by adding more servers or nodes, which is crucial for handling growing data volumes and concurrent users.

- **Flexibility**: They accommodate diverse data types and structures, making them adaptable to changing application requirements without requiring a predefined schema.

- **Performance**: NoSQL databases are optimized for high read/write throughput and low latency, which is beneficial for real-time applications and large-scale data processing.

### Why Learn SQL After NoSQL?

Despite the advantages of NoSQL, SQL (relational databases) remains widely used and important for several reasons:

- **Mature Ecosystem**: SQL databases have a mature ecosystem of tools, libraries, and expertise that support a wide range of applications.

- **Transaction Support**: ACID (Atomicity, Consistency, Isolation, Durability) properties are guaranteed in relational databases, ensuring data integrity and reliability, which is critical for financial transactions and other mission-critical applications.

- **Structured Query Language**: SQL provides a powerful and standardized way to query and manipulate data, which is beneficial for complex queries and reporting.

In conclusion, while NoSQL databases offer significant advantages in scalability, flexibility, and performance for certain use cases, SQL databases continue to play a crucial role in many applications due to their strong consistency guarantees and broad industry adoption. Understanding both SQL and NoSQL enables database developers and administrators to choose the right tool for the job based on specific project requirements.


----------------------------------------------



### 1. Difference between SQL and NoSQL

- **SQL Example**: MySQL is a popular relational database management system (RDBMS) that uses SQL. Here's a simple SQL query:
  ```sql
  SELECT * FROM customers WHERE age > 25;
  ```
  This query selects all customers from the `customers` table where the `age` column is greater than 25.

- **NoSQL Example**: MongoDB, a document-oriented NoSQL database, doesn't use SQL. Instead, it uses a JSON-like query language. Here’s a MongoDB query:
  ```json
  db.customers.find({ "age": { "$gt": 25 } });
  ```
  This finds documents in the `customers` collection where the `age` field is greater than 25.

### 2. ACID (Atomicity, Consistency, Isolation, Durability)

- **Example**: In a banking application (using SQL):
  - **Atomicity**: A transfer between accounts either completes entirely or not at all.
  - **Consistency**: All account balances must reflect correct values after any transaction.
  - **Isolation**: Transactions occur independently without interference.
  - **Durability**: Once a transaction is committed, changes are permanent even in case of system failure.



### ACID Principles in MongoDB:

#### 1. Atomicity:

**Definition**: Atomicity ensures that either all operations within a transaction are successfully completed, or if any operation fails, the entire transaction is rolled back to its initial state.

**Example in MongoDB**:
```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['bank']

# Begin a transaction-like operation (MongoDB does not support traditional transactions)
collection = db['accounts']

# Simulating an atomic update
try:
    with client.start_session() as session:
        # Start transaction
        with session.start_transaction():
            # Perform operations as part of a "transaction"
            collection.update_one({'account_id': 123}, {'$inc': {'balance': -100}})
            collection.update_one({'account_id': 456}, {'$inc': {'balance': 100}})

            # Commit transaction (not a real commit in MongoDB, just for illustration)
            session.commit_transaction()
except Exception as e:
    print(f"Transaction aborted: {e}")
    # Rollback (not a real rollback in MongoDB, just for illustration)
    session.abort_transaction()
```

In MongoDB, transactions are not fully supported in the traditional sense (as of my knowledge cutoff in January 2022), but operations can be grouped logically using sessions to ensure atomicity. The example above demonstrates how you can attempt to update two accounts in a "transactional" manner, ensuring that either both updates succeed or none do.

#### 2. Consistency:

**Definition**: Consistency guarantees that data remains in a valid state before and after the execution of transactions. All constraints and validations are enforced.

**Example in MongoDB**:
```python
# Ensuring consistency in MongoDB
collection = db['accounts']

# Validate account balances after transaction (not a real consistency check, just for illustration)
account_123 = collection.find_one({'account_id': 123})
account_456 = collection.find_one({'account_id': 456})

if account_123['balance'] + account_456['balance'] == 0:
    print("Accounts are consistent after transaction")
else:
    print("Accounts are inconsistent after transaction")
```

In MongoDB, you would typically validate data consistency through application logic rather than relying on built-in database constraints.

#### 3. Isolation:

**Definition**: Isolation ensures that transactions are independent of each other, and operations within a transaction are isolated from other concurrent transactions until they are completed.

**Example in MongoDB**:
```python
# Ensuring isolation in MongoDB
# MongoDB handles isolation at the document level within a single operation or transaction-like session.

# Example of concurrent updates (simplified)
# Assume two threads/processes trying to update the same account simultaneously
def update_balance(account_id, amount):
    collection.update_one({'account_id': account_id}, {'$inc': {'balance': amount}})

# Thread 1
update_balance(123, -100)

# Thread 2 (concurrently)
update_balance(123, -50)
```

MongoDB ensures isolation at the document level, meaning changes within a single operation (like `update_one`) are atomic and isolated from other operations until completed.

#### 4. Durability:

**Definition**: Durability guarantees that once a transaction is committed, it will persist even in the face of system failures (like power outages or crashes).

**Example in MongoDB**:
```python
# Ensuring durability in MongoDB
# MongoDB ensures durability through its storage engine and replication mechanisms.

# Inserting a document
collection = db['logs']
result = collection.insert_one({'event': 'transaction_completed', 'amount': 100})

# Confirming durability
if result.acknowledged:
    print("Document inserted and persisted to disk")
else:
    print("Document insert failed or not yet persisted")
```

MongoDB ensures durability by writing data to disk (depending on the write concern used) and by employing replication across multiple nodes in a cluster, ensuring data redundancy and availability even in the event of hardware failures.

### Conclusion:

While MongoDB does not support traditional ACID transactions in the way SQL databases do (as of the knowledge cutoff), it provides mechanisms and best practices to achieve similar levels of atomicity, consistency, isolation, and durability for applications requiring robust data integrity and reliability. Developers often rely on application-level logic, transactions within sessions, and appropriate write concerns to ensure data safety and consistency in MongoDB deployments.




### 3. Document Storage (Example using MongoDB)

- **Example**: Storing a document in MongoDB:
  ```json
  {
    "_id": ObjectId("60cc3f4fe6a17b731f73baba"),
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "address": {
      "city": "New York",
      "state": "NY",
      "country": "USA"
    }
  }
  ```
  Here, each document is a JSON-like object stored in MongoDB, where fields can vary between documents.

### 4. NoSQL Types

- **Example**: Different types of NoSQL databases include:
  - **Key-Value Store**: Redis (key-value pairs, used for caching)
  - **Document Store**: MongoDB (JSON-like documents, flexible schemas)
  - **Column Store**: Apache Cassandra (optimized for querying columns of data)
  - **Graph Database**: Neo4j (stores data in graph structures for relationships)

### 5. Benefits of a NoSQL Database

- **Example**: Using MongoDB for flexibility and scalability:
  - **Flexible Schema**: Easily adapt data structures as application needs evolve.
  - **Scalability**: Horizontally scale by adding more nodes.
  - **Performance**: Handle large volumes of data with high read/write throughput.

### 6. Querying Information from a NoSQL Database (Using MongoDB)

- **Example**: Querying documents from MongoDB:
  ```javascript
  // Find all documents where age is greater than 25
  db.customers.find({ age: { $gt: 25 } });
  ```
  This retrieves all documents from the `customers` collection where the `age` field is greater than 25.

### 7. Insert/Update/Delete Information from a NoSQL Database (Using MongoDB)

- **Examples**:
  - **Inserting**: Adding a new document to MongoDB:
    ```javascript
    db.customers.insertOne({
      name: "Jane Smith",
      age: 28,
      email: "jane.smith@example.com",
      address: { city: "San Francisco", state: "CA", country: "USA" }
    });
    ```
  - **Updating**: Updating an existing document in MongoDB:
    ```javascript
    db.customers.updateOne(
      { name: "John Doe" },
      { $set: { age: 31, email: "john.doe.updated@example.com" } }
    );
    ```
  - **Deleting**: Removing a document from MongoDB:
    ```javascript
    db.customers.deleteOne({ name: "Jane Smith" });
    ```

### 8. How to Use MongoDB

- **Example**: Connecting to MongoDB and performing basic operations:
  ```javascript
  // Connecting to MongoDB
  const MongoClient = require('mongodb').MongoClient;
  const uri = "mongodb://localhost:27017/mydb";
  const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  // Inserting a document
  client.connect(err => {
    const collection = client.db("mydb").collection("customers");
    collection.insertOne({ name: "Alice", age: 25 });
    
    // Querying documents
    collection.find({}).toArray((err, result) => {
      if (err) throw err;
      console.log(result);
      client.close();
    });
  });
  ```
  This example connects to a MongoDB database, inserts a document, queries all documents, and prints the result.



### Connecting to MongoDB in Python

```python
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Accessing a database
db = client['mydatabase']

# Accessing a collection
collection = db['customers']
```

### 2. Inserting Data into MongoDB

```python
# Inserting a single document
customer_data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com',
    'address': {
        'city': 'New York',
        'state': 'NY',
        'country': 'USA'
    }
}
result = collection.insert_one(customer_data)
print(f'Inserted document id: {result.inserted_id}')
```

### 3. Querying Data from MongoDB

```python
# Finding documents
query = {'age': {'$gt': 25}}
results = collection.find(query)

for document in results:
    print(document)
```

### 4. Updating Data in MongoDB

```python
# Updating a document
update_query = {'name': 'John Doe'}
new_values = {'$set': {'age': 31, 'email': 'john.doe.updated@example.com'}}
collection.update_one(update_query, new_values)

# Confirm update
updated_document = collection.find_one({'name': 'John Doe'})
print('Updated document:', updated_document)
```

### 5. Deleting Data from MongoDB

```python
# Deleting a document
delete_query = {'name': 'John Doe'}
collection.delete_one(delete_query)

# Confirm deletion
remaining_documents = collection.find()
for document in remaining_documents:
    print(document)
```

### 6. Handling MongoDB Documents in Python

MongoDB stores documents in JSON-like format, which can be easily manipulated in Python:

```python
# Accessing fields in a document
document = collection.find_one({'name': 'John Doe'})
if document:
    print('Name:', document['name'])
    print('Age:', document['age'])
    print('Email:', document['email'])
    print('Address:', document['address']['city'], document['address']['state'], document['address']['country'])
```

### 7. Benefits of MongoDB

MongoDB offers flexibility, scalability, and ease of use:

- **Flexible Schema**: Easily adapt data structures without migrations.
- **Scalability**: Horizontally scale by adding more nodes.
- **Performance**: High read/write throughput, suitable for large-scale applications.

### 8. Document Storage in MongoDB

Documents in MongoDB are stored in collections, which are schema-less:

```python
# Example of a MongoDB document in Python
{
    '_id': ObjectId('60cc3f4fe6a17b731f73baba'),
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@example.com',
    'address': {
        'city': 'New York',
        'state': 'NY',
        'country': 'USA'
    }
}
```

These Python examples demonstrate basic operations with MongoDB, showcasing its document-oriented nature and how Python can interact with MongoDB using the `pymongo` library. Each example illustrates concepts like querying, updating, deleting, and handling MongoDB documents.

----------------------------------------


Certainly! Let's cover various MongoDB operations with commands and examples. We'll go through listing databases and collections, inserting data, finding documents, matching criteria, counting documents, updating documents, and deleting documents (both single and multiple).

### 1. Listing Databases and Collections

#### List all databases
```bash
show databases
```

#### List all collections in a database (e.g., `mydb`)
```bash
use mydb
show collections
```

### 2. Inserting Data

#### Insert a single document into a collection
```bash
use mydb
db.customers.insertOne({ "name": "John Doe", "age": 30 })
```

#### Insert multiple documents into a collection
```bash
db.customers.insertMany([
    { "name": "Jane Smith", "age": 25 },
    { "name": "Bob Johnson", "age": 35 }
])
```

### 3. Finding Documents and Matching Criteria

#### Find all documents in a collection
```bash
db.customers.find()
```

#### Find documents matching specific criteria (e.g., age greater than 30)
```bash
db.customers.find({ "age": { $gt: 30 } })
```

### 4. Counting Documents

#### Count all documents in a collection
```bash
db.customers.count()
```

#### Count documents matching specific criteria (e.g., age greater than 30)
```bash
db.customers.count({ "age": { $gt: 30 } })
```

### 5. Updating Documents

#### Update a single document
```bash
# Update the document where name is "John Doe"
db.customers.updateOne(
    { "name": "John Doe" },
    { $set: { "age": 31 } }
)
```

#### Update multiple documents (all documents that match the query)
```bash
# Update all documents where age is less than 30
db.customers.updateMany(
    { "age": { $lt: 30 } },
    { $set: { "category": "Young Adult" } }
)
```

### 6. Deleting Documents

#### Delete a single document
```bash
# Delete the document where name is "Jane Smith"
db.customers.deleteOne({ "name": "Jane Smith" })
```

#### Delete multiple documents (all documents that match the query)
```bash
# Delete all documents where age is greater than or equal to 40
db.customers.deleteMany({ "age": { $gte: 40 } })
```

### 7. Using `$set` and `multi` Option (with `true` or `false`)

#### Using `$set` to update specific fields in a document
```bash
# Update the document where name is "John Doe" to set the field "status" to "active"
db.customers.updateOne(
    { "name": "John Doe" },
    { $set: { "status": "active" } }
)
```

#### Using `multi` with `true` to update multiple documents
```bash
# Update all documents where age is greater than 30 to set the field "category" to "Senior"
db.customers.updateMany(
    { "age": { $gt: 30 } },
    { $set: { "category": "Senior" } },
    { multi: true }
)
```

In MongoDB, the `multi` option is used in update operations to specify whether the update should affect multiple documents that match the query criteria (`true`) or just the first document found (`false`, which is the default behavior if `multi` is not explicitly specified).

### Understanding `multi` in MongoDB Updates:

#### 1. `multi: true`

When you set `multi: true` in an update operation, MongoDB will update all documents that match the query criteria. This means:

- **Update Multiple Documents**: If your update query matches multiple documents in the collection, all of these documents will be updated according to the specified update operation.

#### Example:

```bash
# Update all documents where age is greater than 30 to set the field "category" to "Senior"
db.customers.updateMany(
    { "age": { $gt: 30 } },
    { $set: { "category": "Senior" } },
    { multi: true }
)
```

In this example:
- `multi: true` ensures that all documents where `"age"` is greater than 30 will have their `"category"` field updated to `"Senior"`.

#### 2. `multi: false`

By default, MongoDB assumes `multi: false` if it's not explicitly stated. This means:

- **Update Only the First Matching Document**: MongoDB will update only the first document that matches the query criteria. Subsequent documents that also match the criteria will not be updated.

#### Example:

```bash
# Update the first document where age is less than 25 to set the field "category" to "Junior"
db.customers.updateOne(
    { "age": { $lt: 25 } },
    { $set: { "category": "Junior" } },
    { multi: false }
)
```

In this example:
- `multi: false` ensures that only the first document found where `"age"` is less than 25 will have its `"category"` field updated to `"Junior"`. If there are multiple documents with `"age"` less than 25, only the first one encountered in the collection will be updated.

### Choosing Between `multi: true` and `multi: false`

- **Use `multi: true`** when you want to update multiple documents that match your query criteria across the entire collection.
  
- **Use `multi: false`** (or simply omit the `multi` option) when you only want to update the first document that matches your query criteria, especially useful when ensuring unique updates or when you know only one document should match the query.







#### Using `multi` with `false` (default) to update only the first matching document
```bash
# Update the first document where age is less than 25 to set the field "category" to "Junior"
db.customers.updateOne(
    { "age": { $lt: 25 } },
    { $set: { "category": "Junior" } },
    { multi: false }
)
```

### 8. Deleting Many Documents

#### Delete all documents in a collection
```bash
db.customers.deleteMany({})
```






To connect MongoDB to Python and perform operations like `find`, `insert`, `insert_one`, `update_many`, `find` with specific criteria, and `count_documents`, you'll use the `pymongo` library.:


### 1. Install pymongo

If you haven't installed `pymongo` yet, you can install it using pip:

```bash
pip install pymongo
```

### 2. Connect to MongoDB

To connect to MongoDB from Python, you'll typically specify the connection string and initialize a client instance:

```python
# main.py

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
```

Replace `'mongodb://localhost:27017/'` with your MongoDB connection string if it's hosted elsewhere.

### 3. Perform Operations: `find`, `insert`, `insert_one`, `update_many`, `count_documents`

#### a. Inserting Data (`insert_one` and `insert_many`)

```python
# Inserting one document
def insert_one_example():
    db = client['mydatabase']
    collection = db['customers']
    
    document = { "name": "John Doe", "age": 30 }
    result = collection.insert_one(document)
    print(f"Inserted document id: {result.inserted_id}")

# Inserting multiple documents
def insert_many_example():
    db = client['mydatabase']
    collection = db['customers']
    
    documents = [
        { "name": "Jane Smith", "age": 25 },
        { "name": "Bob Johnson", "age": 35 }
    ]
    result = collection.insert_many(documents)
    print(f"Inserted {len(result.inserted_ids)} documents")
```

#### b. Updating Data (`update_many`)

```python
# Updating multiple documents
def update_many_example():
    db = client['mydatabase']
    collection = db['customers']
    
    result = collection.update_many(
        { "age": { "$gt": 30 } },  # Filter criteria
        { "$set": { "category": "Senior" } }  # Update operation
    )
    print(f"Matched {result.matched_count} documents and modified {result.modified_count} documents")
```

#### c. Finding Data (`find` and `find_one`)

```python
# Finding documents with specific criteria
def find_with_criteria_example():
    db = client['mydatabase']
    collection = db['customers']
    
    # Find documents where age is greater than 30
    cursor = collection.find({ "age": { "$gt": 30 } })
    
    for document in cursor:
        print(document)
        
# Finding a single document
def find_one_example():
    db = client['mydatabase']
    collection = db['customers']
    
    # Find the first document in the collection
    document = collection.find_one()
    if document:
        print(document)
    else:
        print("No document found")
```

#### d. Counting Documents (`count_documents`)

```python
# Counting documents with specific criteria
def count_documents_example():
    db = client['mydatabase']
    collection = db['customers']
    
    # Count documents where age is greater than 30
    count = collection.count_documents({ "age": { "$gt": 30 } })
    print(f"Number of documents where age > 30: {count}")
```

### 4. Running `main.py`

Now, create a `main.py` file and call these functions to execute the operations:

```python
# main.py

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

def insert_one_example():
    db = client['mydatabase']
    collection = db['customers']
    
    document = { "name": "John Doe", "age": 30 }
    result = collection.insert_one(document)
    print(f"Inserted document id: {result.inserted_id}")

def insert_many_example():
    db = client['mydatabase']
    collection = db['customers']
    
    documents = [
        { "name": "Jane Smith", "age": 25 },
        { "name": "Bob Johnson", "age": 35 }
    ]
    result = collection.insert_many(documents)
    print(f"Inserted {len(result.inserted_ids)} documents")

def update_many_example():
    db = client['mydatabase']
    collection = db['customers']
    
    result = collection.update_many(
        { "age": { "$gt": 30 } },
        { "$set": { "category": "Senior" } }
    )
    print(f"Matched {result.matched_count} documents and modified {result.modified_count} documents")

def find_with_criteria_example():
    db = client['mydatabase']
    collection = db['customers']
    
    cursor = collection.find({ "age": { "$gt": 30 } })
    
    for document in cursor:
        print(document)

def find_one_example():
    db = client['mydatabase']
    collection = db['customers']
    
    document = collection.find_one()
    if document:
        print(document)
    else:
        print("No document found")

def count_documents_example():
    db = client['mydatabase']
    collection = db['customers']
    
    count = collection.count_documents({ "age": { "$gt": 30 } })
    print(f"Number of documents where age > 30: {count}")

if __name__ == "__main__":
    insert_one_example()
    insert_many_example()
    update_many_example()
    find_with_criteria_example()
    find_one_example()
    count_documents_example()
```

### Explanation:

- **Connect to MongoDB**: Use `MongoClient` to establish a connection to your MongoDB instance.
  
- **Insert Operations**: Use `insert_one` to insert a single document and `insert_many` to insert multiple documents into a collection.

- **Update Operations**: Use `update_many` to update multiple documents that match specific criteria.

- **Find Operations**: Use `find` to query documents based on criteria and `find_one` to retrieve a single document.

- **Count Operation**: Use `count_documents` to count documents that match specific criteria.

### Running the Script:

Save `main.py` and execute it. This script will demonstrate MongoDB operations from Python, showing how to connect, insert data, update data, find data, and count documents based on your requirements. Adjust the database name (`mydatabase`), collection name (`customers`), and document structure as per your MongoDB setup.



### 1. `$regex` for Pattern Matching

**Usage**: The `$regex` operator is used for pattern matching strings using regular expressions.

**When to use**: Use `$regex` when you need to search for documents where a field matches a specific pattern.

**Example**:

```python
# main.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['customers']

# Finding documents where the name field matches a pattern
def find_with_regex_example():
    pattern = "^J"  # Pattern to match names starting with 'J'
    cursor = collection.find({ "name": { "$regex": pattern } })
    
    for document in cursor:
        print(document)

if __name__ == "__main__":
    find_with_regex_example()
```

### 2. `$project` to Include or Exclude Fields

**Usage**: The `$project` operator is used in aggregation to include or exclude specific fields from the documents.

**When to use**: Use `$project` to transform the documents by including or excluding fields, often to reduce the size of the returned documents or to format the output.

**Example**:

```python
# main.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['customers']

# Projecting specific fields
def project_example():
    cursor = collection.aggregate([
        { "$project": { "name": 1, "age": 1, "_id": 0 } }  # Include name and age, exclude _id
    ])
    
    for document in cursor:
        print(document)

if __name__ == "__main__":
    project_example()
```

### 3. `$avg` to Calculate the Average

**Usage**: The `$avg` operator is used in aggregation to calculate the average of numerical values.

**When to use**: Use `$avg` to compute the average value of a numeric field across multiple documents.

**Example**:

```python
# main.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['customers']

# Calculating the average age
def average_example():
    cursor = collection.aggregate([
        { "$group": { "_id": None, "average_age": { "$avg": "$age" } } }
    ])
    
    for document in cursor:
        print(f"Average age: {document['average_age']}")

if __name__ == "__main__":
    average_example()
```

### 4. `$sort` to Sort Documents

**Usage**: The `$sort` operator is used to sort the documents in ascending (`1`) or descending (`-1`) order based on one or more fields.

**When to use**: Use `$sort` to order the documents based on specific fields.

**Example**:

```python
# main.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['customers']

# Sorting documents by age in ascending order
def sort_example():
    cursor = collection.find().sort("age", 1)  # 1 for ascending, -1 for descending
    
    for document in cursor:
        print(document)

if __name__ == "__main__":
    sort_example()
```

### 5. `aggregate()` Function for Advanced Queries

**Usage**: The `aggregate()` function is used to process data through a pipeline of stages, including `$match`, `$group`, `$project`, `$sort`, and more.

**When to use**: Use `aggregate()` for complex queries that require multiple stages of data transformation and aggregation.

**Example**:

```python
# main.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['customers']

# Using aggregate to find average age and sort by name
def aggregate_example():
    pipeline = [
        { "$match": { "age": { "$gt": 20 } } },  # Match documents where age is greater than 20
        { "$group": { "_id": None, "average_age": { "$avg": "$age" } } },  # Calculate average age
        { "$sort": { "name": 1 } },  # Sort documents by name in ascending order
        { "$project": { "name": 1, "average_age": 1, "_id": 0 } }  # Project specific fields
    ]
    
    cursor = collection.aggregate(pipeline)
    
    for document in cursor:
        print(document)

if __name__ == "__main__":
    aggregate_example()
```

### Summary

- **`$regex`**: Pattern matching in queries.
- **`$project`**: Include or exclude fields in the result.
- **`$avg`**: Calculate the average of a numeric field.
- **`$sort`**: Sort documents based on a field.
- **`aggregate()`**: Perform advanced data processing and transformation through a pipeline of stages.

Each of these operators and functions serves specific purposes in querying and transforming data in MongoDB. Using them effectively can greatly enhance your data retrieval and processing capabilities in `pymongo`.


----------------------------------------


To establish a relationship between Nginx and MongoDB in a Python application, we can create a simple web application that uses Nginx as a reverse proxy server to route requests to a Python backend, which then interacts with MongoDB to handle CRUD operations. Below is a detailed explanation with examples on how to achieve this.

### Prerequisites

- **Nginx**: Installed and configured on your server.
- **MongoDB**: Running instance.
- **Python**: Installed with necessary packages (`Flask` and `pymongo`).

### Step-by-Step Guide

1. **Set Up MongoDB and Python Backend**:
   We'll use `Flask` to create a simple RESTful API that interacts with MongoDB using `pymongo`.

2. **Configure Nginx as a Reverse Proxy**:
   Nginx will forward incoming HTTP requests to our Flask application.

### Python Backend with Flask and PyMongo

1. **Install Required Packages**:
   Ensure you have Flask and PyMongo installed:
   ```bash
   pip install flask pymongo
   ```

2. **Create a Flask Application**:
   Below is a `main.py` file implementing basic CRUD operations (GET, POST, PUT, PATCH, DELETE) with MongoDB.

```python
# main.py
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['customers']

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = list(collection.find({}, {'_id': 0}))
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({'message': 'Customer added', 'id': str(result.inserted_id)}), 201

@app.route('/customers/<name>', methods=['PUT'])
def update_customer(name):
    data = request.json
    result = collection.update_one({'name': name}, {'$set': data})
    return jsonify({'message': 'Customer updated' if result.modified_count > 0 else 'No changes made'}), 200

@app.route('/customers/<name>', methods=['PATCH'])
def patch_customer(name):
    data = request.json
    result = collection.update_one({'name': name}, {'$set': data})
    return jsonify({'message': 'Customer partially updated' if result.modified_count > 0 else 'No changes made'}), 200

@app.route('/customers/<name>', methods=['DELETE'])
def delete_customer(name):
    result = collection.delete_one({'name': name})
    return jsonify({'message': 'Customer deleted' if result.deleted_count > 0 else 'Customer not found'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Nginx Configuration

1. **Install Nginx**:
   If you don't have Nginx installed, you can install it using:
   ```bash
   sudo apt update
   sudo apt install nginx
   ```

2. **Configure Nginx as a Reverse Proxy**:
   Create a new configuration file for your Flask application, typically located in `/etc/nginx/sites-available/`.

   Example configuration `/etc/nginx/sites-available/flask_app`:
   ```nginx
   server {
       listen 80;
       server_name your_domain_or_IP;

       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

3. **Enable the Configuration and Restart Nginx**:
   Create a symbolic link to enable the site and restart Nginx.
   ```bash
   sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled/
   sudo nginx -t  # Test the configuration for syntax errors
   sudo systemctl restart nginx
   ```

### Testing the Application

1. **Start the Flask Application**:
   ```bash
   python main.py
   ```

2. **Make Requests**:
   You can use tools like `curl` or Postman to make requests to your Nginx server, which will forward the requests to your Flask application.

   **GET Request**:
   ```bash
   curl http://your_domain_or_IP/customers
   ```

   **POST Request**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice", "age": 28}' http://your_domain_or_IP/customers
   ```

   **PUT Request**:
   ```bash
   curl -X PUT -H "Content-Type: application/json" -d '{"age": 29}' http://your_domain_or_IP/customers/Alice
   ```

   **PATCH Request**:
   ```bash
   curl -X PATCH -H "Content-Type: application/json" -d '{"age": 30}' http://your_domain_or_IP/customers/Alice
   ```

   **DELETE Request**:
   ```bash
   curl -X DELETE http://your_domain_or_IP/customers/Alice
   ```

### Summary

- **Nginx** serves as a reverse proxy, forwarding requests to the Flask backend.
- **Flask** handles the HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) and interacts with MongoDB.
- **PyMongo** is used for performing CRUD operations on MongoDB.
- **Nginx Configuration** ensures that the requests are properly routed to the Flask application running on a specific port.

This setup allows you to build a robust application where Nginx efficiently handles incoming traffic and routes it to your Python-based backend which performs database operations on MongoDB.
