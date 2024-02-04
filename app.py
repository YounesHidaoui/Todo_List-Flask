# Importing necessary modules from flask, flask_sqlalchemy and flask_marshmallow
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Creating an instance of Flask
app = Flask(__name__)


# Running the app
if __name__ == '__main__':
    app.run(debug=True)
