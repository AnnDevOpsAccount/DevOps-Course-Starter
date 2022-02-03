from flask import Flask, render_template, request
from todo_app.data import session_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = session_items.get_items()
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