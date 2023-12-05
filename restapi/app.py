from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hotels(Resource):
    def get(self):
        return {'hotels': 'my hotels'}


class NoPath(Resource):
    def get(self):
        return {'status': 'up and running'}


api.add_resource(Hotels, '/hotels')
api.add_resource(NoPath, '/')

if __name__ == '__main__':
    app.run(debug=True)
