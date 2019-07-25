import pymongo
# without creating collection and insert data database name and collection not show
import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017')
mydb=myclient['mydatabase']
print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
else:
    print("The database Not exists.")