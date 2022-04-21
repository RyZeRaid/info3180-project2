from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,IntegerField, SelectField,FloatField, SubmitField, TextAreaField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, DataRequired, Length, Email


class addCarsForm(FlaskForm):
    description  =TextAreaField('description',validators=[DataRequired(),InputRequired(),Length(max=800)] )
    make = StringField('Make', validators=[InputRequired()])
    modle = StringField('Modle',validators=[InputRequired()])
    color = StringField('Color', validators=[InputRequired()])
    year = StringField('year', validators=[InputRequired()])
    transmition = StringField('Transmition', validators=[InputRequired()])
    car_type = StringField('Type', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    photo = FileField('Photo ', validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    user_id = IntegerField('user ID',validators=[InputRequired()])

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
    