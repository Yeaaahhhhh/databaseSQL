from pymongo import MongoClient

fileList = ["artists.json", "tracks.json"]
client = MongoClient('mongodb://localhost:27017')
database = client["A4dbNorm"]
collectionA = database['Artists']

#finalPrint = {'artist_id':1, 'name':1, 'num_tracks' : {'$size': '$tracks'}}
#requirement = {'$where':'this.tracks.length >= 1'}
finalPrint = {"NumBranches": {"$sum": "$followers"}}
#requirement = {"name":"Sucks","popularity":900,"followers":{"$gt":2}}
for i in collectionA.find(finalPrint):
    print(i)