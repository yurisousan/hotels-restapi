from flask import Flask
from flask_restful import Api

from resources.hotel import Hotels, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_request
def create_database():
    database.create_all()


# class NoPath(Resource):
#     def get(self):
#         return {'status': 'up and running'}


api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')
# api.add_resource(NoPath, '/')

if __name__ == '__main__':
    from sql_alch import database
    database.init_app(app)
    app.run(debug=True)
