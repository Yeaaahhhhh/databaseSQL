from pymongo import MongoClient


fileList = ["artists.json", "tracks.json"]
client = MongoClient('mongodb://localhost:27017')
database = client["A4dbEmbed"]
collectionA = database['ArtistsTracks']

finalPrint = {"$group": {"_id": "$artist_id", "total_length": {"$sum": "$tracks.duration"}, "artist_ids": {"$first": "$artist_id"}}}
for i in collectionA.aggregate([{"$unwind": "$tracks"},finalPrint]):
    print(i)
