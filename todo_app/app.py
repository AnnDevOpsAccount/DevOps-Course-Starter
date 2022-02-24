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
    trello_items.add_item(  app.config['TRELLO_BOARD_KEY'],
                            app.config['TRELLO_BOARD_TOKEN'],
                            app.config['TRELLO_TO_DO_LIST_ID'],
                            request.form['TaskName'] )
    return index()
    
@app.route('/endTask', methods=['POST'])
def end_task():
    trello_items.complete_item(  app.config['TRELLO_BOARD_KEY'],
                            app.config['TRELLO_BOARD_TOKEN'],
                            app.config['TRELLO_DONE_LIST_ID'],
                            request.form['TaskNo'] )
    return index()