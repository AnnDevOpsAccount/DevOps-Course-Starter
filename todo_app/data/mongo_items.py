import pymongo
from flask import Flask
from todo_app.flask_config import Config



def add_item( app, title):
    client = pymongo.MongoClient(app.config['MONGO_CONNECTION_STRING'])
    db = client[app.config['MONGO_DATABASE']]
    collection = db['Items']
    item1 = {"title": title, "status:": "To Do"}
    collection.insert_one(item1)

    #delete an old one
#    myquery = { "title": "earn money" }
#    collection.delete_one(myquery)

    # print it to see if it worked?
    for x in collection.find():
        print(x)

