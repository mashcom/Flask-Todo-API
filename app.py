from flask import Flask, jsonify, request, json
from apps.todo.models import Task
from database import db_session

app = Flask(__name__)
app.debug = True

'''
Get a all todo items
'''
@app.route('/todo', methods=['GET'])
def index():
    tasks = Task.query.all()
    response = list(map(lambda task: task.serialize(), tasks))
    return jsonify(response)

'''
Get a single todo item
'''
@app.route('/todo/<todo_id>')
def show(todo_id):
    task = Task.query.get(todo_id)
    return task.as_dict()


'''
Add a new todo item
'''
@app.route('/todo', methods=['POST'])
def store():
    task = Task()
    task.title = request.form['title']
    task.description = request.form['description']
    task.status = request.form['status']
    task.start_date = request.form['start_date']
    db_session.add(task)
    db_session.commit()
    return {'success': task.id is not int, 'data': task.as_dict()}


'''
Delete a todo item
'''
@app.route('/todo/<int:id>', methods=['DELETE'])
def destroy(id):
    task = Task.query.get(id)
    db_session.delete(task)
    deleted = db_session.commit()
    return {'success': deleted is None, 'data': task.as_dict()}


'''
Change status of a todo item
'''
@app.route('/todo/<int:id>/done', methods=['PATCH'])
def update_status(id):
    task = Task.query.get(id)
    task.status = "completed"
    updated = db_session.commit()
    return {'success': updated is None, 'data': task.as_dict()}


'''
Get information about the todo api
'''
@app.route('/todo/about')
def about():
    return {'name': 'A simple Todo API in Flask', 'version': '0.1.0'}


if __name__ == '__main__':
    app.run(debug=True)
