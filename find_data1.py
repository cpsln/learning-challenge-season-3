# find the specifice data with given condition

import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclient['mydatabase1']
mycol=mydb['customers']

myquery={"address":"Green Grass 1"}

x=mycol.find(myquery)
for i in x:
    print(i)