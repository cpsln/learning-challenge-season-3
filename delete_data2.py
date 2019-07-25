# delete all document of collection of database
import pymongo
myclt=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclt['mydatabase']
mycl=mydb['customers']

x=mycl.delete_many({})
print(x.deleted_count,'document deleted')