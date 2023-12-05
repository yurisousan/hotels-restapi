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
        return {'hotels': hotels}


class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name')
    arguments.add_argument('stars')
    arguments.add_argument('diary')
    arguments.add_argument('city')

    def find_hotel(hotel_id):
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                return hotel

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):

        data = Hotel.arguments.parse_args()

        obj_hotel = HotelModel(hotel_id, **data)
        new_hotel = obj_hotel.json()

        hotels.append(new_hotel)
        return new_hotel, 200

    def put(self, hotel_id):

        data = Hotel.arguments.parse_args()

        obj_hotel = HotelModel(hotel_id, **data)
        new_hotel = obj_hotel.json()

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(new_hotel)
            return new_hotel, 200
        hotels.append(new_hotel)
        return new_hotel, 201

    def delete(self, hotel_id):
        global hotels
        hotels = [hotel for hotel in hotels if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted'}
