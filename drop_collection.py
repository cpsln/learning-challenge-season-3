# drop collection of database
import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclient['mydatabase']
mycol=mydb['customers']

if mycol.drop():
    print('collection drop of mydatabase')
else:
    print('collection " not " drop of mydatabase')