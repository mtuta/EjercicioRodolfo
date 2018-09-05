"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,jsonify, request, Flask, abort,json
from ApiRestPython import app


KEY_VAULT_URI = None
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
    
@app.route('/modelos')
def awesome():
    """Renders modelos"""
    return render_template(
        'modelo.html',
        title='MODELO ML',
    )

#----
@app.route('/postprueba', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    print('Recieved from client: {}'.format(request.data))
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 200
