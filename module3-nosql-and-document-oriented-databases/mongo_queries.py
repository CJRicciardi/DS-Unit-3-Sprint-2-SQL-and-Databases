# mongo_queires.py
# mongo string: mongodb+srv://ricciardistg:<password>@cluster0-iwobt.mongodb.net/test?retryWrites=true&w=majority
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("mongo_user", default="oops")
db_password = os.getenv("mongo_password", default="oops")
cluster_name = os.getenv("mongo_cluster_name", default="oops")

connection_uri = f"mongodb+srv://{db_user}:{db_password}@{cluster_name}.mongodb.net/test?retryWrites=true&w=majority"
print("------------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("------------------")
print("CLIENT:", type(client), client)

db = client.test_database  # we can name test_database what ever we want
print("------------------")
print("DB:", type(db), db)

collection = (
    db.pokemon_collection
)  # again pokemon_collection can get what ever name we want
print("------------------")
print("COLLECTION:", type(collection), collection)

print("------------------")
print("COLLECTIONS:")
print(db.list_collection_names())

collection.insert_one(
    {
        "name": "Pikachu",
        "level": 30,
        "exp": 76000000000,
        "hp": 400,
        "metadata": {"a": "something", "b": "something else"},
    }
)  # we can insert documents nd different structures too

collection.insert_one(
    {"name": "Bulbasaur", "level": 15, "experience": 4000000, "hp": 300,}
)

print("------------------")
print("COLLECTIONS:")
print(db.list_collection_names())

print('DOCS:", collection.count_documents({})')
print(
    "PIKA DOC:", collection.count_documents({"name": "Pikachu"})
)  # like a where clause w/ filter conditions
print(
    "LOW LEVELS:", collection.count_documents({"level": {"$lt": 25}})
)  # like a where clause with filter conditions

print("------------------")
print("INSERT MANY...")

new_documents = [
    {"name": "Snorlax", "lvl": 70},
    {"name": "Charmander", "level": 100},
    {"name": "Jigglypuff", "level": 50},
]

collection.insert_many(new_documents)

print("DOCS:", collection.count_documents({}))  # SELECT *
print(
    "ANY LEVELS:", collection.count_documents({"level": {"$gt": 0}})
)  # like a where clause with filter conditions
