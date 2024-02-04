# Importing necessary modules from flask, flask_sqlalchemy and flask_marshmallow
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Creating an instance of Flask
app = Flask(__name__)
# Configuring the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# Creating an instance of SQLAlchemy
db = SQLAlchemy(app)
# Creating an instance of Marshmallow
ma = Marshmallow(app)

# Defining the Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each task
    task = db.Column(db.String(120), unique=True)  # Task description

# Defining the Todo schema
class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'task')  # Fields to expose

# Creating an instance of TodoSchema
todo_schema = TodoSchema()
# Creating an instance of TodoSchema for multiple todos
todos_schema = TodoSchema(many=True)

# Route to add a new todo
@app.route('/todo', methods=['POST'])
def add_todo():
    task = request.json['task']  # Get task from request
    new_todo = Todo(task=task)  # Create new Todo object
    db.session.add(new_todo)  # Add new Todo to the session
    db.session.commit()  # Commit the session
    return todo_schema.jsonify(new_todo)  # Return the new Todo

# Route to get all todos
@app.route('/todo', methods=['GET'])
def get_todos():
    all_todos = Todo.query.all()  # Query all Todos
    result = todos_schema.dump(all_todos)  # Dump the result
    return jsonify(result)  # Return the result

# Route to get a specific todo
@app.route('/todo/<id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get(id)  # Get Todo by id
    return todo_schema.jsonify(todo)  # Return the Todo

# Route to update a specific todo
@app.route('/todo/<id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get(id)  # Get Todo by id
    task = request.json['task']  # Get task from request
    todo.task = task  # Update the task
    db.session.commit()  # Commit the session
    return todo_schema.jsonify(todo)  # Return the updated Todo

# Route to delete a specific todo
@app.route('/todo/<id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get(id)  # Get Todo by id
    db.session.delete(todo)  # Delete the Todo
    db.session.commit()  # Commit the session
    return todo_schema.jsonify(todo)  # Return the deleted Todo

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
