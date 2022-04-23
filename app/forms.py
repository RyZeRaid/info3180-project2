from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,IntegerField, SelectField,FloatField, SubmitField, TextAreaField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, DataRequired, Length, Email


class addCarsForm(FlaskForm):
    description  =TextAreaField('description',validators=[DataRequired(),InputRequired(),Length(max=800)] )
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model',validators=[InputRequired()])
    colour = StringField('Colour', validators=[InputRequired()])
    year = StringField('year', validators=[InputRequired()])
    transmission = StringField('Transmission', validators=[InputRequired()])
    type = StringField('Type', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    photo = FileField('Photo ', validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    user_id = StringField('user ID',validators=[InputRequired()])

class registerForm(FlaskForm):
    description = TextAreaField('description',validators=[DataRequired(),InputRequired(),Length(max=800)] )
    photo = FileField('Photo ', validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired(),Email('Please enter a valid email adress')])
    location =StringField('Location',  validators=[DataRequired(),InputRequired(),Length(max=700)])
    name = StringField('Fullname', validators=[InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    