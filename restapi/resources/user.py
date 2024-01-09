from flask_restful import Resource, reqparse
from models.user import UserModel
from blacklist import BLACKLIST
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
import hmac

str_to_bytes = lambda s: s.encode("utf-8") if isinstance(s, str) else s
safe_str_cmp = lambda a, b: hmac.compare_digest(str_to_bytes(a), str_to_bytes(b))

attributes = reqparse.RequestParser()
attributes.add_argument(
    'login',
    type=str,
    required=True,
    help="The field Login cannot be left blank"
)
attributes.add_argument(
    'password',
    type=str,
    required=True,
    help="The field Password cannot be left blank"
)


class User(Resource):
    # /users/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404

    @jwt_required()
    def delete(self, user_id):
        hotel = UserModel.find_user(user_id)
        if hotel:
            try:
                hotel.delete_user()
            except Exception:
                return {
                    "message": "An error ocurred trying to delete user."
                }, 500
            return {'message': 'User deleted'}, 200
        return {"message": "User not found"}, 404


class UserRegister(Resource):
    # /register
    def post(self):
        data = attributes.parse_args()

        if UserModel.find_by_login(data['login']):
            return {
                "message": f"The login '{data['login']}' already exists."
            }

        user = UserModel(**data)
        user.save_user()
        return {"message": "User created successfully"}, 201


class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = attributes.parse_args()

        user = UserModel.find_by_login(data['login'])

        if user and safe_str_cmp(user.password, data['password']):
            access_token = create_access_token(identity=user.user_id)
            return {'access_token': access_token}, 200
        return {'message': 'The username or password is incorrect.'}, 401



class UserLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully'}, 200
    