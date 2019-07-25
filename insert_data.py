import pymongo

# connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# create database
mydb = myclient["mydatabase"]

# create collection of database(mydatabase)
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

# insert data into customer collection of mydatabase
x = mycol.insert_one(mydict)

print('Database names: ',myclient.list_database_names())
collist = mydb.list_collection_names()
print('Collection name: ',collist)
print('Id : ',x.inserted_id)

# show the database exit or not

dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
else:
    print("The database Not exists.")

# show the collection name of database exit or not

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
else:
    print("The collection not exists.")