# delete many data from database
import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclient['mydatabase1']
mycol=mydb['customers']

myquery={'address':{'$regex':'^S'}}
x=mycol.delete_many(myquery)
print(x.deleted_count,'document deleted')

for i in mycol.find():
    print(i)