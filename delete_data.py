# delete the specific data
import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclient['mydatabase1']
mycol=mydb['customers']

# delete data

myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)
for s in mycol.find():
    print(s)

