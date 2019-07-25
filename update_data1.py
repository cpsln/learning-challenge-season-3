# update many value of collection
import pymongo
myclient=pymongo.MongoClient('mongodb://collection:27017/')
mydb=myclient['mydatabase1']
mycol=mydb['customers']

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
'''print('---------- before update all data from database ----------------\n')
for i in mycol.find():
    print(i)'''

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

'''print('----------after update all data from database ----------------\n')
for i in mycol.find():
    print(i)'''