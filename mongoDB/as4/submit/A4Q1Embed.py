from pymongo import MongoClient


fileList = ["artists.json", "tracks.json"]
client = MongoClient('mongodb://localhost:27017')
database = client["A4dbEmbed"]
collectionA = database['ArtistsTracks']

finalPrint = {'artist_id':1, 'name':1, 'num_tracks' : {'$size': '$tracks'}}
requirement = {'$where':'this.tracks.length >= 1'}
for track in collectionA.find(requirement, finalPrint):
    print(track)