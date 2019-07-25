# update the data ofcollection
import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017')
mydb=myclient['mydatabase1']
mycol=mydb['customers']

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery,newvalues)

print('---------- all data from database ----------------\n')
for i in mycol.find():
    print(i)