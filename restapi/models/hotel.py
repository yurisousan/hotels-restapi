from sql_alch import database


class HotelModel(database.Model):

    __tablename__ = 'hotels'

    hotel_id = database.Column(database.String, primary_key=True)
    name = database.Column(database.String(80))
    stars = database.Column(database.Float(precision=1))
    diary = database.Column(database.Float(precision=2))
    city = database.Column(database.String(80))

    def __init__(self, hotel_id, name, stars, diary, city):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.diary = diary
        self.city = city

    def json(self):
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "stars": self.stars,
            "diary": self.diary,
            "city": self.city
        }

    @classmethod
    def find_hotel(cls, hotel_id):
        # SELETEC * FROM hotels WHERE hotel_id = $hotel_id LIMIT 1
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        database.session.add(self)
        database.session.commit()

    def update_hotel(self, name, stars, diary, city):
        self.name = name
        self.stars = stars
        self.diary = diary
        self.city = city

    def delete_hotel(self):
        database.session.delete(self)
        database.session.commit()