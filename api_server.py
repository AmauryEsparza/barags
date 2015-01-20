#!flask/bin/python
from flask import Flask, request
import json
from bson import json_util
from bson.objectid import ObjectId
from pymongo import Connection
from flask import abort
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)

# MongoDB connection
connection = Connection('localhost', 27017)
db = connection.pubs
def toJson(data):
    """Convert Mongo object(s) to JSON"""
    return json.dumps(data, default=json_util.default)

@app.route('/api/pubs', methods=['GET'])
def get_pubs():
    if request.method == 'GET':
        results = db['pubsData'].find()
        json_results = []
        for result in results:
            json_results.append(result)
        return toJson(json_results)

#@app.route('/api/pubs/<int:pub_id>', methods=['GET'])
#def get_pub(pub_id):
    #pub = [pub for pub in pubs if pub['id'] == pub_id]
    #if len(pub) == 0:
        #abort(404)
    #return jsonify({'pub': pub[0]})

if(__name__ == '__main__'):
    app.run()

    #pubs = [
    #{
        #'id': 1,
        #'pub_name': u'Bar Nacional',
        #'description': u'Amplio bar con terraza y ambiente musical alternativo',
        #'phone': 4491234567,
        #'address': u'Madero #103 Col. Centro',
        #'beer_price': 20.00,
        #'shot_price': 35.00
    #},
    #{
        #'id': 2,
        #'pub_name': u'Micheladas Galerias',
        #'description':u'Lugar para bailar con tambora en vivo',
        #'address': u'C.C Galerias',
        #'phone': 4498765124,
        #'beer_price': 35.00,
        #'shot_price': 40.00
    #},
    #{
        #'id': 3,
        #'pub_name': u'Los Remedios de Pachita',
        #'description':u'Atractivo lugar con musica electronica',
        #'address': u'Madero #200 Col. Centro',
        #'phone': 4491111111,
        #'beer_price': 30.00,
        #'shot_price': 70.00
    #}
#]