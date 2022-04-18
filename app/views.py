"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request,jsonify, redirect, url_for,flash,send_from_directory
import os
from .models import Cars,Users
from .forms import addCarsForm, registerForm
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from datetime import date, datetime
from flask_login import login_user, logout_user, current_user, login_required
from flask_wtf.csrf import generate_csrf

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

@app.route('/api/register',methods = ["POST","GET"])
def register():
    form = registerForm()
    if request.method == 'POST'and form.validate_on_submit():
        
        description = form.description.data
        name = form.name.data
        location= form.location.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        photo.save((os.path.join(app.config['UPLOAD_FOLDER'], filename)))

        
          
        user = Users(name = name, biography = description , password = password,
                        email = email,location = location, username = username, photo = filename) 
        print("before database", user)
        db.session.add(user)
        db.session.commit()
        
        flash('Successfully added a new member to the database','success')
        return jsonify(message="This is the register of our API", filename = filename,
                        biography = description, name=name, location= location, email= email, username=username, password=password)
    else:
        flash('ERROR didnt add image','danger')
        return jsonify(errors = form_errors(form))    
        

@app.route('/api/auth/login',methods = ["POST","GET"])
def login():
    return jsonify(message="This is the login of our API")

@app.route('/api/auth/logout',methods= ["POST","GET"])
def logout():
    return jsonify(message="This is the logout of our API")

@app.route('/api/cars')
def showcars():
    return jsonify(message="This is the show cars of our API")

@app.route('/api/cars', methods= ["POST","GET"])
def addcars():
    return jsonify(message="This is the addcars of our API")

@app.route('/api/cars/<int:id>',methods= ["POST","GET"])
def viewcar(id):
    return jsonify(message="This is the view a car of our API")

@app.route('/api/cars/<int:id>/favourite',methods= ["POST","GET"])
def addfavcar(id):
    return jsonify(message="This is the add to favourite of our API")   

@app.route('/api/cars',methods= ["POST","GET"])
def search():
    return jsonify(message="This is the search cars of our API")

@app.route('/api/users/<int:id>',methods= ["POST","GET"])
def viewuser(id):
    return jsonify(message="This is the see users info of our API")

@app.route('/api/users/<int:id>/favourites',methods= ["POST","GET"])
def getfavcar(id):
    return jsonify(message="This is the get users favourite cars of our API")

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def get_uploaded_images():
    rootdir = os.getcwd()
    print("this is root" ,rootdir)
    file_store=[]
    for subdir, dirs, files in os.walk('uploads'):
        for file in files:
            file_store.append(os.path.join(subdir, file))
    return file_store

def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")