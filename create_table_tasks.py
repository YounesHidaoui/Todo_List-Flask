from flask import Flask
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
@app.route('/create_table', methods=['GET'])
def create_table():
    cur = mysql.connection.cursor()
    cur.execute("CREATE TABLE tasks (id INT AUTO_INCREMENT PRIMARY KEY, task VARCHAR(255))")
    mysql.connection.commit()
    cur.close()
    return 'Table created successfully', 200



if __name__ == "__main__":
    app.run(debug=True)