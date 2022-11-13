from pymongo import MongoClient
from bson.json_util import loads
import datetime
fileList = ["artists.json", "tracks.json"]
client = MongoClient('mongodb://localhost:27017')
database = client["A4dbEmbed"]
collectionA = database['ArtistsTracks']

finalPrint = {"_id": 1,"name": 1,"t_name": "$tracks.name","t_release_date": "$tracks.release_date"}
whichdDate =  datetime.datetime(1950, 1, 1, 0, 0)

for i in collectionA.aggregate([{"$unwind": "$tracks"},{"$match": {"tracks.release_date": {"$gt":whichdDate}}},{"$project": finalPrint},{"$sort": {"t_release_date": 1}}]):
    print(i)
