from flask import Flask, render_template, request
from todo_app.data import trello_items
from todo_app.flask_config import Config
import os
import requests

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    return render_template('index.html', 
                            items=trello_items.get_items( app.config['TRELLO_BOARD_KEY'], 
                                                          app.config['TRELLO_BOARD_TOKEN']) )

@app.route('/addTask', methods=['POST'])
def add_task():
    new_task = request.form['TaskName']
    trello_items.add_item(  app.config['TRELLO_BOARD_KEY'],
                            app.config['TRELLO_BOARD_TOKEN'],
                            app.config['TRELLO_TO_DO_LIST_ID'],
                            new_task )
    return index()
    
@app.route('/endTask', methods=['POST'])
def end_task():
    #item_to_Update = session_items.get_item(request.form['TaskNo'])
    #item_to_Update.update({"status":"complete"})
    #session_items.save_item(item_to_Update)
    return index()