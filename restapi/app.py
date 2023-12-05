from flask import Flask
from flask_restful import Api

from resources.hotel import Hotels, Hotel

app = Flask(__name__)
api = Api(app)


# class NoPath(Resource):
#     def get(self):
#         return {'status': 'up and running'}


api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')
# api.add_resource(NoPath, '/')

if __name__ == '__main__':
    app.run(debug=True)
