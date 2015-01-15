#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

pubs = [
    {
        'id': 1,
        'pub_name': u'Bar Nacional',
        'description': u'Amplio bar con terraza y ambiente musical alternativo',
        'phone': 4491234567,
        'beer_price': 20.00,
        'shot_price': 35.00
    },
    {
        'id': 2,
        'pub_name': u'Micheladas Galerias',
        'description':u'Lugar para bailar con tambora en vivo',
        'phone': 4498765124,
        'beer_price': 35.00,
        'shot_price': 40.00
    },
    {
        'id': 3,
        'pub_name': u'Los Remedios de Pachita',
        'description':u'Atractivo lugar con musica electronica',
        'phone': 4491111111,
        'beer_price': 30.00,
        'shot_price': 70.00
    }
]

@app.route('/api/pubs', methods=['GET'])
def get_pubs():
    return jsonify({'pubs': pubs})

if(__name__ == '__main__'):
    app.run()