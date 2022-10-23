import pymongo

client = pymongo.MongoClient("mongodb://aaaddd000444000999:wGsud7sTDAMvHb7qwo5nnpcP2Mok8O0bmY2uuEPuNnViIv8vqv5sTlnmC5XkwSOvVbH4dhIMIPt5oDymzDAToQ==@aaaddd000444000999.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@aaaddd000444000999@")
db = client['ad0409todoappdb']
collection = db['Items']

def add_item( title):
    item1 = {"title": title, "status:": "To Do"}
    collection.insert_one(item1)

    #delete an old one
#    myquery = { "title": "earn money" }
#    collection.delete_one(myquery)

    # print it to see if it worked?
    for x in collection.find():
        print(x)

