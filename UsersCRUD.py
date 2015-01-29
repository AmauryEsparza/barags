#!flask/bin/python
from flask import jsonify
from pymongo import Connection
from flask import abort

# MongoDB connection
connection = Connection('localhost', 27017)
db = connection.baragsDB

class UsersCRUD:
    def __init__(self):
        self

    def getUsers():
        users = db.users.find()
        if len(users) > 1:
            json_results = []
            for user in users:
                json_results.append(user)
            return json_results
        else:
            abort(500)