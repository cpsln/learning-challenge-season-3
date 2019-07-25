import pymongo

myclient=pymongo.MongoClient('mongodb://localhost:27017')
# without creating collection and insert data database name and collection not show
import pymongo
mydb=myclient['mydatabase']
mycol=mydb['customers']
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
else:
    print("The collection not exists.")