from pymongo import MongoClient
import datetime

fileList = ["artists.json", "tracks.json"]
client = MongoClient('mongodb://localhost:27017')
database = client["A4dbNorm"]
collectionA = database['Tracks']

matchDic = {"from": "Artists","localField": "artist_ids","foreignField": "artist_id","as": "track_info"}
finalPrint = {"_id": 1,"name": "$track_info.name","t_name": "$name","t_release_date": "$release_date"}
whichdDate =  datetime.datetime(1950, 1, 1, 0, 0)
final = collectionA.aggregate([{"$match": {"release_date": {"$gt": whichdDate}}},{"$lookup":matchDic},{"$unwind": "$track_info"},{"$project":finalPrint},{"$sort": {"_id": -1}}]) 

for i in final:
    print(i)