"""
By Samir and Adrian Marin Estrada
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Dedomena(Resource):
    def get(self):
        return {'hello': 'dedomena'}

api.add_resource(Dedomena, '/')

if __name__ == '__main__':
    app.run(debug=True)