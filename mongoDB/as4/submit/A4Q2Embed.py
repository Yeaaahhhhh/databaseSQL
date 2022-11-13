from pymongo import MongoClient

client = MongoClient()
db = client["A4dbEmbed"]
collection = db['ArtistsTracks']

requirement = {"tracks.track_id": {"$regex": '^70'}}
finalPrint = {"$group": {"_id": "", "avg_danceability": {"$avg": "$tracks.danceability"}}}
for i in collection.([{"$unwind": "$tracks"},{"$match": requirement},finalPrint]):
    print(i)
