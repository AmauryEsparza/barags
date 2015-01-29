#!flask/bin/python
from flask import Flask, request
from flask import jsonify
import json
from bson import json_util

from pymongo import Connection
from flask import abort
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)

# MongoDB connection
connection = Connection('localhost', 27017)
db = connection.baragsDB
def toJson(data):
    """Convert Mongo object(s) to JSON"""
    return json.encoder(data, default=json_util.default)

#Get the pubs
@app.route('/api/pubs', methods=['GET'])
def get_pubs():
    if request.method == 'GET':
        results = db['pubs'].find()
        json_results = []
        for result in results:
            json_results.append(result)
        return jsonify(pubs=str(json_results))

#Get the specific pub
@app.route('/api/pubs/<int:index>', methods=['GET'])
def get_pub(index):
    if request.method == 'GET':
        pubs = db['pubs'].find()
        pub = pubs[index]
        if len(pub) > 1:
            return jsonify(pub=str(pub))
        else:
            abort(500)
        #return jsonify(pub=str(pubs[index]))

#Post a pub
@app.route('/api/pubs', methods=['POST'])
def insert_pub():
    #Verify the method (GET or POST)
    if request.method == 'POST':
        pub = request.get_json(force=True)
        #If the request have more than one field
        if len(pub) > 1:
            pubs = db.pubs
            post_id = pubs.insert(pub)
            if len(str(post_id)) == 0:
                abort(500)
            else:
                return jsonify(mns200="Added")
        else:
            print "Need at least one field"
            abort(400)

#Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    if request.method == 'GET':
        users = db.users.find()
        json_results = []
        for user in users:
            json_results.append(user)
        return jsonify(user=str(json_results))

#Get specific user
@app.route('/api/users/<int:index>', methods=['GET'])
def get_user(index):
    if request.method == 'GET':
        users = db.users.find()
        user = users[index]
        if len(user) > 1:
            return jsonify(user=str(user))
        else:
            abort(500)

#Post a user
@app.route('/api/users', methods=['POST'])
def insert_user():
    if request.method == 'POST':
        user = request.get_json(force=True)
        #If the request have more than one field
        if len(user) > 1:
            users = db.users
            post_id = users.insert(user)
            if len(str(post_id)) == 0:
                abort(500)
            else:
                return jsonify(mns200="Added")
        else:
            print "Need at least one field"
            abort(400)

if(__name__ == '__main__'):
    app.run()