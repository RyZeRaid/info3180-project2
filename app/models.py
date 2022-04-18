from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash

class Cars(db.Model):

    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100),nullable=False)
    make = db.Column(db.String(100),nullable=False)
    model = db.Column(db.String(100),nullable=False)
    color = db.Column(db.String(100),nullable=False)
    year = db.Column(db.String(100),nullable=False)
    transmission = db.Column(db.String(100),nullable=False)
    car_type = db.Column(db.String(100),nullable=False)
    price = db.Column(db.Float ,nullable=False)
    photo = db.Column(db.String(100),nullable=False)
    user_id = db.Column(db.Integer,nullable=False)

    def __init__(self, description, make, model, color, year, transmission, car_type, price, photo, user_id):
        self.description = description
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.car_type = car_type
        self.price = price
        self.photo = photo
        self.user_id = user_id

class Favourites(db.Model):

    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer,nullable=False)

    def __init__(self, car_id,user_id):
        self.car_id = car_id
        self.user_id = user_id

class Users(db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(140),nullable=False)
    biography = db.Column(db.String(800),nullable=False)
    photo = db.Column(db.Text,nullable=False)
    date_joined = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, username, password, email , name, location, biography, photo):
        self.name = name
        self.username = username
        self.location = location
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.biography = biography
        self.photo = photo


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.username