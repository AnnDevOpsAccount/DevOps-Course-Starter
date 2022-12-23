from flask import Flask, redirect, render_template, request
from flask_login import LoginManager, UserMixin, login_required, login_user
from todo_app.flask_config import Config
from todo_app.data import mongo_items
import os
import requests
import pymongo
from todo_app.viewModel import ViewModel

def create_app():
    print("hello")
    app = Flask(__name__)  
    app.config.from_object(Config())
    login_manager = LoginManager()

    @login_manager.unauthorized_handler
    def unauthenticated():
        print("hello1")
        redirect_url = f"https://github.com/login/oauth/authorize?client_id={os.getenv('GITHUB_CLIENT_ID')}"
        return redirect(redirect_url)

    @login_manager.user_loader
    def load_user(user_id):
        print("hello2")
        pass # We will return to this later

    login_manager.init_app(app)

    @app.route('/')
    @login_required
    def index():
        print("hello3")        
        item_view_model = ViewModel(app)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/login/callback')
    def callback():
        print("hello4")
        authorisation_code = request.args['code']
        access_token_url = f"https://github.com/login/oauth/access_token"
        query_params = {
            "client_id": os.getenv('GITHUB_CLIENT_ID'),
            "client_secret": os.getenv('GITHUB_CLIENT_SECRET'),
            "code": authorisation_code
        }
        headers = { "Accept": "application/json" }
        access_token_response = requests.post(access_token_url, params = query_params, headers = headers)
        access_token = access_token_response.json()['access_token']
        user_info_url = "https://api.github.com/user"
        auth_headers = { "Authorization": f"Bearer {access_token}" }
        user = requests.get(user_info_url, headers = auth_headers)
        print("user")
        return redirect('/')

    @app.route('/addTask', methods=['POST'])
    @login_required
    def add_task():
        print("hello5")
        mongo_items.add_item(app, request.form['TaskName'])
        return index()
 
    @app.route('/endTask', methods=['POST'])
    @login_required
    def end_task():
        print("hello6")
        mongo_items.complete_item(app, request.form['TaskName'])
        return index()

    return app