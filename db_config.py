from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db =  client['personal_notes_manager']
notes_collection= db['notes']
user_collection= db['user']