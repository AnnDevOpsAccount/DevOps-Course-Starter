from flask import Flask, render_template, request
from todo_app.flask_config import Config
from todo_app.data import mongo_items
import os
import requests
import pymongo
from todo_app.viewModel import ViewModel

def create_app():
    app = Flask(__name__)  
    app.config.from_object(Config())

    @app.route('/')
    def index():
        item_view_model = ViewModel(app)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/addTask', methods=['POST'])
    def add_task():
        mongo_items.add_item(app, request.form['TaskName'])
        return index()
        
    @app.route('/endTask', methods=['POST'])
    def end_task():
        mongo_items.complete_item(app, request.form['TaskName'])
        return index()

    return app