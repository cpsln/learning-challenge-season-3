# find where address start with 'S'
import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclient['mydatabase1']
mycol=mydb['customers']

myquery={'address':{"$gt": "S" }}
x=mycol.find(myquery)
for i in x:
    print(i)

print('\n--------------with regular expretion-----------------\n')
myquery = { "address": { "$regex": "^S" } }
x=mycol.find(myquery)
for i in x:
    print(i)