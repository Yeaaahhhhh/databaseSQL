from pymongo import MongoClient


fileList = ["artists.json", "tracks.json"]
client = MongoClient('mongodb://localhost:27017')
database = client["A4dbNorm"]
collectionA = database['Tracks']

finalPrint ={"_id": 1,"artist_id": "$_id","total_length": 1}

for i in collectionA.aggregate([{"$unwind": "$artist_ids"},{"$group": {"_id": "$artist_ids","total_length": {"$sum": "$duration"}}},{"$project": finalPrint}]):
    print(i)

