from flask import Flask, render_template, request
from todo_app.data import session_items
from todo_app.flask_config import Config
import os
import requests

app = Flask(__name__)
app.config.from_object(Config())
url = "https://api.trello.com/1/boards/6212689e46f57218f07af552/lists/open"

@app.route('/')
def index():
    querystring = { "key": os.getenv("TRELLO_BOARD_KEY"),
                    "token":os.getenv("TRELLO_BOARD_TOKEN"),
                    "cards":"open"}
    response = requests.request("GET", url, params=querystring)
    response_json = response.json() 
    items = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            print (card)
            card['status'] = trello_list['name']
            card['title'] = card ['name']
            items.append(card)
    return render_template('index.html', items=items)

@app.route('/addTask', methods=['POST'])
def add_task():
    new_task = request.form['TaskName']
    session_items.add_item(new_task)
    return index()
    
@app.route('/endTask', methods=['POST'])
def end_task():
    item_to_Update = session_items.get_item(request.form['TaskNo'])
    item_to_Update.update({"status":"complete"})
    session_items.save_item(item_to_Update)
    return index()







   