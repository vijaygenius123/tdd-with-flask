from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)

api = Api(app)

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong'
        }


api.add_resource(Ping,'/ping')