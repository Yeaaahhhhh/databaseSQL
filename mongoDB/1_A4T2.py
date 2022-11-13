from pymongo import MongoClient
import json

client = MongoClient('localhost',27017)
db = client['collection_A']
collection1 = db['collection1']


with open('artists.json') as f1:
    f1dic = json.load(f1)
    f1dic = dict(f1dic)
    
result = db.test.insert_one(f1dic)
print(result.insert_id)