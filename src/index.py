# pylint: disable=unused-import
import geojson
from flask import Flask, request
from flask_restx import Api, Resource
from flask_cors import CORS

from models.user import User
import fetch_from_museovirasto
import mongo

app = Flask(__name__)
api = Api(app)

CORS(app)


@api.route('/api/helloworld')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}


@api.route('/api/healthcheck')
class HealthCheck(Resource):
    def get(self):
        return {'status': 'ok'}


@api.route('/api/data')
class Data(Resource):
    def get(self):
        with open('data/wreckdata.json', encoding='utf8') as file:
            geojsonfile = geojson.load(file)
        return geojsonfile

    def update(self):
        fetch_from_museovirasto.save_wrecks_geojson('data')
        return {'status': 'update done'}


@api.route('/api/dive')
class Dive(Resource):
    def get(self):
        pass

    def post(self):
        pass


@api.route('/api/users')
class Users(Resource):
    def get(self):
        users = User.to_json()
        return {'data': users}

    def post(self):
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        User.create(first_name, last_name, email)
        return {'status': 'ok'}, 201


if __name__ == '__main__':
    app.run(debug=True)
