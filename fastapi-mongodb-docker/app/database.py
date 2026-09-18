import os
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://db:27017")
MONGO_DATABASE = os.getenv("MONGO_DATABASE", "fastapi_db")

client = MongoClient(MONGO_URL)
database = client[MONGO_DATABASE]
items_collection = database["items"]
