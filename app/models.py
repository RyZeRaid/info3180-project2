from distutils.archive_util import make_archive
from pyexpat import model
from . import db

class Cars(db.Model):

    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100),nullable=False)
    make = db.Column(db.String(100),nullable=False)
    model = db.Column(db.String(100),nullable=False)
    colour = db.Column(db.String(100),nullable=False)
    year = db.Column(db.String(100),nullable=False)
    transmission = db.Column(db.String(100),nullable=False)
    car_type = db.Column(db.String(100),nullable=False)
    price = db.Column(db.Float ,nullable=False)
    photo = db.Column(db.String(100),nullable=False)
    user_id = db.Column(db.Integer,nullable=False)

    def __init__(self, description, make, model, colour, year, transmission, car_type, price, photo, user_id):
    self.description = description
    self.make = make
    self.model = model
    self.colour = colour
    self.year = year
    self.transmission = transmission
    self.car_type = car_type
    self.price = price
    self.photo = photo
    self.user_id = user_id