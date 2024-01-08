from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.hotel import Hotels, Hotel
from resources.user import User, UserRegister, UserLogin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
api = Api(app)
jwt = JWTManager(app)


@app.before_request
def create_database():
    database.create_all()


# class NoPath(Resource):
#     def get(self):
#         return {'status': 'up and running'}


api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
# api.add_resource(NoPath, '/')

if __name__ == '__main__':
    from sql_alch import database
    database.init_app(app)
    app.run(debug=True)
