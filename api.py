"""
By Samir and Adrian Marin Estrada
"""
from createDatabaseHelper import list_of_files
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Dedomena(Resource):
    def get(self):
        return {'hello': 'dedomena'}

# path_name is a string
# gets list of files
class CreateDatabase(Resource):
	def get(self, path_name):
		# print(path_name)
		return list_of_files(path_name)
		# return "Hello!"

api.add_resource(CreateDatabase,'/<string:path_name>')
api.add_resource(Dedomena, '/')

if __name__ == '__main__':
    app.run(debug=True)