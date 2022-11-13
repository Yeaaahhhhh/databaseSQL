from pymongo import MongoClient
from bson.json_util import loads

fileList = ["artists.json", "tracks.json"]
client = MongoClient('mongodb://localhost:27017')
db = client["A4dbEmbed"]
collection = db["ArtistsTracks"]

with open(fileList[0], encoding="utf8") as file1:
    data1 = loads(file1.read())
with open(fileList[1], encoding="utf8") as file2:
    data2 = loads(file2.read())

for i in range(len(data1)):
    for j in range(len(data1[i]['tracks'])):
        track_id = data1[i]['tracks'][j]
        for track in data2:
            if track['track_id'] == track_id:
                data1[i]['tracks'][j] = track
collection.insert_many(data1)
