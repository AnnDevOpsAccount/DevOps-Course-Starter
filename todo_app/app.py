from flask import Flask, render_template, request
from todo_app.flask_config import Config
from todo_app.data import trello_items
from todo_app.data import mongo_items
import os
import requests
import pymongo
from todo_app.board import Board
from todo_app.viewModel import ViewModel

def create_board(app):
    app.config.from_object(Config())
    return Board ( app.config['TRELLO_BOARD_ID'], 
                app.config['TRELLO_BOARD_KEY'], 
                app.config['TRELLO_BOARD_TOKEN'], 
                app.config['TRELLO_TO_DO_LIST_ID'], 
                app.config['TRELLO_DONE_LIST_ID'])

def create_app():
    app = Flask(__name__)  
    board = create_board(app)  

    @app.route('/')
    def index():
        item_view_model = ViewModel(board)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/addTask', methods=['POST'])
    def add_task():
        trello_items.add_item(board , request.form['TaskName'])

        #WIP lets try also add in Mongo
        mongo_items.add_item(app, request.form['TaskName'])
        return index()
        
    @app.route('/endTask', methods=['POST'])
    def end_task():
        trello_items.complete_item(board, request.form['TaskNo'])
        return index()

    return app