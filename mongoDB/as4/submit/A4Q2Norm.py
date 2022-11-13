from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client["A4dbNorm"]
collection = db["Tracks"]

finalPrint = {"$group": {"_id": '', "avg_danceability": {"$avg": "$danceability"}}}
requirement = {"track_id": {"$regex": '^70'}}
for i in collection.aggregate([{"$match": requirement}, finalPrint]):
    print(i)
