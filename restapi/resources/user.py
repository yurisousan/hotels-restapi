from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument(
        'name',
        type=str,
        required=True,
        help="This field 'name' cannot be left blank."
    )
    arguments.add_argument(
        'stars',
        type=float,
        required=True,
        help="This field 'stars' cannot be left blank."
    )
    arguments.add_argument('diary')
    arguments.add_argument('city')

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'Hotel not found.'}, 404

    def delete(self, user_id):
        hotel = UserModel.find_user(user_id)
        if hotel:
            try:
                hotel.delete_user()
            except Exception:
                return {
                    "message": "An error ocurred trying to delete hotel."
                }, 500
            return {'message': 'Hotel deleted'}, 200
        return {"message": "Hotel not found"}, 404
