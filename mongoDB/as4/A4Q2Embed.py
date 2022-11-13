import json

from bson import json_util
from pymongo import MongoClient
import bson
from bson.json_util import loads, dumps

# Use client = MongoClient('mongodb://localhost:27017') for specific ports!
# Connect to the default port on localhost for the mongodb server.
client = MongoClient()

# create a database named A4dbNorm on server.
db = client["A4dbNorm"]

# create a collection "Artist"
collection_A = db['Artist']

# create a collection "Tracks"
collection_T = db['Tracks']

# delete all previous entries in the collection
# specify no condition.

collection_A.delete_many({})
collection_T.delete_many({})


# open file 1
with open('artists.json', 'r', encoding='UTF-8') as f1:
    # using json_util's helper loads
    f1_data = json.loads(f1.read(), object_hook=json_util.object_hook)
# for loop to insert to collection
for data1 in f1_data:
    collection_A.insert_one(data1)

# open file 2
with open('tracks.json', 'r', encoding='UTF-8') as f2:
    # using json_util's helper loads
    f2_data = json.loads(f2.read(),object_hook=json_util.object_hook)
# for loop to insert to collection
for data2 in f2_data:
    collection_T.insert_one(data2)
    
client.close()