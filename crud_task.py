from flask import Flask
from flask_mysqldb import MySQL
from flask import request

app = Flask(__name__)

# Required
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "todo_list"
# Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes

mysql = MySQL(app)

@app.route('/task', methods=['POST'])
def create_task():
     
    task = request.json['task']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tasks(task) VALUES (%s)", [task])
    mysql.connection.commit()
    cur.close()
    return 'success', 200


# Route to get all todos
@app.route('/todo', methods=['GET'])

def get_todos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    return ({'tasks': tasks}), 200
# Route to get a specific todo
@app.route('/todo/<id>', methods=['GET'])
def get_todo(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks WHERE id = %s", [id])
    todo = cur.fetchone()
    cur.close()
    return ({'todo': todo}), 200

# Route to update a specific todo
@app.route('/todo/<id>', methods=['PUT'])
def update_todo(id):
    cur = mysql.connection.cursor()
    task = request.json['task']  # Get task from request
    cur.execute("UPDATE tasks SET task = %s WHERE id = %s", (task, id))  # Update the task
    mysql.connection.commit()  # Commit the session
    cur.close()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks WHERE id = %s", [id])
    todo = cur.fetchone()
    cur.close()
    return ({'todo': todo}), 200  # Return the updated Todo

# Route to delete a specific todo
@app.route('/todo/<id>', methods=['DELETE'])
def delete_todo(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    return 'Task deleted successfully', 200

    
# Running the app
if __name__ == '__main__':
    app.run(debug=True)
