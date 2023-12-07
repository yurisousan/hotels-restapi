from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hotels = [
    {
        'hotel_id': 'alpha',
        'name': 'Alpha Hotel',
        'stars': 4.3,
        'diary': 420.34,
        'city': 'Sao Paulo'
    },
    {
        'hotel_id': 'bravo',
        'name': 'Bravo Hotel',
        'stars': 4.4,
        'diary': 400,
        'city': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'delta',
        'name': 'Delta Hotel',
        'stars': 4.5,
        'diary': 421,
        'city': 'Minas Gerais'
    }
]


class Hotels(Resource):
    def get(self):
        return {'hotels': [hotel.json() for hotel in HotelModel.query.all()]}


class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name')
    arguments.add_argument('stars')
    arguments.add_argument('diary')
    arguments.add_argument('city')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {
                "message": "Hotel id '{}' already exists.".format(hotel_id)
            }, 400
        data = Hotel.arguments.parse_args()
        hotel = HotelModel(hotel_id, **data)
        hotel.save_hotel()
        return hotel.json()

    def put(self, hotel_id):
        data = Hotel.arguments.parse_args()

        hotel_founded = HotelModel.find_hotel(hotel_id)
        if hotel_founded:
            hotel_founded.update_hotel(**data)
            hotel_founded.save_hotel()
            return hotel_founded.json(), 200
        hotel = HotelModel(hotel_id, **data)
        hotel.save_hotel()
        return hotel.json(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel deleted'}, 200
        return {"message": "Hotel not found"}, 404
