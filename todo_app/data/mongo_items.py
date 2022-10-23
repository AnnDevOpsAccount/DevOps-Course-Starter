import pymongo
from flask import Flask
from todo_app.flask_config import Config



def add_item(app, title):
    client = pymongo.MongoClient(app.config['MONGO_CONNECTION_STRING'])
    db = client[app.config['MONGO_DATABASE']]
    collection = db['Items']
    newItem = {"title": title, "status:": "To Do"}
    collection.insert_one(newItem)

    #delete an old one
    #myquery = { "title": "get on with it" }
    #collection.delete_one(myquery)

    # print it to see if it worked?
    for x in collection.find():
        print(x)

def complete_item(app, title):
    client = pymongo.MongoClient(app.config['MONGO_CONNECTION_STRING'])
    db = client[app.config['MONGO_DATABASE']]
    collection = db['Items']
    myquery = { "title": title, "status:": "To Do"}
    collection.delete_one(myquery)
    newItem = {"title": title, "status:": "Done"}
    collection.insert_one(newItem)

    # print it to see if it worked?
    for x in collection.find():
        print(x)