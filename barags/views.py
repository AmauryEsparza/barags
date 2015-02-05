#!flask/bin/python
from flask import request, jsonify, abort, Response
from bson.json_util import dumps
from flask.ext.httpauth import HTTPBasicAuth
from barags import app
from . import db

auth = HTTPBasicAuth()

#Get the pubs
@app.route('/api/pubs', methods=['GET'])
def get_pubs():
    if request.method == 'GET':
        results = db['pubs'].find()
        json_results = []
        for result in results:
            json_results.append(result)
        return Response(dumps(json_results), mimetype='application/json')
        #return jsonify(json_results)

#Get the specific pub
@app.route('/api/pubs/<int:index>', methods=['GET'])
def get_pub(index):
    if request.method == 'GET':
        pubs = db['pubs'].find()
        pub = pubs[index]
        return Response(dumps(pub), mimetype='application/json')
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
                return jsonify({'success': True}), 200
        else:
            print "Need at least one field"
            abort(400)

#Delete a pub
@app.route('/api/pubs/<int:index>', methods=['DELETE'])
def delete_pub(index):
    if request.method == 'DELETE':
        pubs = db.pubs.find()
        pub_id = pubs[index].get('_id')
        #If the user exists
        if(pub_id):
            status = db.pubs.remove({'_id': pub_id})
            print status
            if (status is None):
                print "Se elimino correctamente"
                return jsonify({'success': True}), 200
            else:
                print "No se pudo eliminar"
                abort(400)
        else:
            abort(200)
    else:
        abort(400)

#Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    if request.method == 'GET':
        users = db.users.find()
        json_results = []
        for user in users:
            json_results.append(user)
        return Response(dumps(json_results), mimetype="application/json")
        #return jsonify(user=str(json_results))

#Get specific user
@app.route('/api/users/<int:index>', methods=['GET'])
def get_user(index):
    if request.method == 'GET':
        users = db.users.find()
        user = users[index]
        return Response(dumps(user), mimetype="application/json")

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
                return jsonify({'status', True}, 200)
        else:
            print "Need at least one field"
            abort(400)

#Delete a user
@app.route('/api/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if request.method == 'DELETE':
        users = db.users.find()
        user_id = users[index].get('_id')
        #If the user exists
        if(user_id):
            status = db.users.remove({'_id': user_id})
            print status
            if (status is None):
                print "Se elimino correctamente"
                return jsonify({'success': True}), 200
            else:
                print "No se pudo eliminar"
                abort(400)
        else:
            abort(200)
    else:
        abort(400)

@app.route('/api/repo', methods=['GET'])
def get_repo():
    jsonA = {'id': 1, 'name': "AmauryEsparza.io"}
    return jsonify(jsonA)

