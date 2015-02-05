from flask import Flask
from pymongo import Connection
#Run the Flask server
app = Flask(__name__)
# MongoDB connection
connection = Connection('localhost', 27017)
db = connection.baragsDB
#Like instance views package
from . import views