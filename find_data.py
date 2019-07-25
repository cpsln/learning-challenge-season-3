import pymongo
myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb=myclient['mydatabase1']
mycol=mydb['customers']

# find one data from customers collection of mydatabase1
print('-----------one database from customers collection of mydatabase1------------\n')
x=mycol.find_one()
print(x)

# find all data from customers collection of mydatabase1
print('\n----------- All database from customers collection of mydatabase1------------\n')
for x in mycol.find():
  print(x)

# Return only the names and addresses, not the _ids
print('\n-------------Name and address---------------\n')
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

# Return only the names and ids
print('\n-------------Name and Ids---------------\n')
for x in mycol.find({},{ "address":0 }):
  print(x)
