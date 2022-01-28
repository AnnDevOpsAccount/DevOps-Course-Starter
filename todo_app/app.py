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
def addTask():
    newTask = request.form['TaskName']
    session_items.add_item(newTask)
    return index()
    
@app.route('/endTask', methods=['POST'])
def endTask():
    itemToUpdate = session_items.get_item(request.form['TaskNo'])
    itemToUpdate.update({"status":"complete"})
    session_items.save_item(itemToUpdate)
    return index()