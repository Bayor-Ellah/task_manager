from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

#connect to mongo atlas cluster
mongo_client = MongoClient(os.getenv("MONGO_URL"))


# Access database
task_manager_db = mongo_client["task_manager_db"]


# Pick a collection to operate on
tasks = task_manager_db["tasks"]