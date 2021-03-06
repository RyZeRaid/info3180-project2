"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request,jsonify, redirect, url_for,flash,send_from_directory,session,send_file
import os
from .models import Cars, Users, Favourites, cars_schema
from .forms import addCarsForm, registerForm, LoginForm, SearchForm
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from datetime import date, datetime
from flask_login import login_user, logout_user, current_user, login_required
from flask_wtf.csrf import generate_csrf

# Routing for your application.
###

@app.route('/api/users/<int:id>/favourites',methods= ["POST","GET"])
def getfavcar(id):
    
    

    cars = []

    favs = Favourites.query.filter_by(user_id = id).all()

    for fav in favs:
        car = Cars.query.filter_by(id = fav.car_id).all()
        print(car)
        cars += (car)

    carsschema = cars_schema(many = True)
    carss = carsschema.dump(cars)
    print(cars)
    return jsonify(carss)

@app.route('/api/users/<int:id>',methods= ["POST","GET"])
def viewuser(id):
    print(id)
    user = Users.query.get_or_404(id)
    return jsonify(username = user.username, email = user.email, name = user.name, location = user.location, biography = user.biography, photo = user.photo, date_joined = user.date_joined)

@app.route('/api/cars/<int:id>/<int:user_id>', methods= ["POST","GET"])
def viewcar(id,user_id):
    carsschema = cars_schema(many = True)
    fav = False
    cars =  Cars.query.get_or_404(id)
    check = Favourites.query.filter_by(car_id = id).all()
    check_id = Favourites.query.filter_by(user_id = user_id).all()
    
    if check_id == None and check == None:
        fav = False
    elif check_id == None :
        fav = False
    else:
        for i in check_id:
            for x in check:
                if x.car_id == i.car_id and x.user_id == i.user_id:
                    fav = True
            
    print(cars)
    
    #carss = carsschema.dump(cars)

    'id','description', 'make', 'model', 'color', 'year', 'transmission', 'car_type', 'price', 'photo'

    return jsonify(make = cars.make, id = cars.id, description = cars.description, model = cars.model, color = cars.color, year = cars.year, transmission = cars.transmission, car_type = cars.car_type, price = cars.price, photo = cars.photo,fav = fav)

@app.route('/api/cars', methods=['GET'])
def showcars():

    carsschema = cars_schema(many = True)

    cars =  Cars.query.all()

    print(cars)

    carss = carsschema.dump(cars[-3:])
    return jsonify(carss)

@app.route('/')
def index():
 return send_file(os.path.join('../dist/', 'index.html'))
 
@app.route('/about')
def about():
    return jsonify(message="This is the beginning of our testing thsi ")

@app.route('/api/register',methods = ["POST","GET"])
def register():
    print("this is the register form ")
    form = registerForm()
    user= None
    re =user
    
    if form.validate_on_submit() and request.method == 'POST':
        description = form.description.data
        name = form.name.data
        location= form.location.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)
        
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        user = Users(
                    biography=description,name=name, location=location,
                    email=email, photo =filename, password=password,username=username 
        ) 
            
        db.session.add(user)
        db.session.commit()
        flash('Successfully added a new member to the database','success')
        re= user
        return jsonify({
                            'message':'This is the register of our API ',
                            
        })
    else:
        return jsonify(message= "error ", user = re)


@app.route('/api/addcar',methods = ["POST","GET"])
def addcar():
    
    form = addCarsForm()
    car = None
    re = car
   
    if request.method == 'POST':
        
        description = form.description.data
        photo = form.photo.data
        make = form.make.data
        model = form.model.data
        colour = form.colour.data
        transmission = form.transmission.data
        car_type = form.type.data
        year = form.year.data
        price = form.price.data
        filename = secure_filename(photo.filename)
        print("this is the path", os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("this is it")
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        id = form.user_id.data

        car = Cars(
                    description=description,make=make, model= model,
                    color=colour, photo =filename, transmission = transmission,car_type=car_type, price = price, user_id = id, year = year
        ) 
            
        db.session.add(car)
        db.session.commit()
        flash('Successfully added a car to the database','success')
        re = car
        return jsonify({
                            'message':'This is the register of our API ',
        })
    else:
        return jsonify(message= "error ")
       
        

@app.route('/api/auth/login',methods = ["POST","GET"])
def login():

    print("got in function",request.method)
    res = {'status': 'success wasnt true'}
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        
        username = form.username.data
        password = form.password.data
        print(username, password, "this is the info entered")
        user = Users.query.filter_by(username=username).first()
        print("this is the user")

        if user is not None and check_password_hash(user.password, password):
           
            next_page = request.args.get('next')
        
            res = { 'token': user.password ,
                    'id': user.id,
                    'auth': True }
            
        else:
            print("no user with that password ")
            flash('Username or Password is incorrect.', 'danger')
            res = { 'token': '' ,
                    'id': '',
                    'auth': False }
    return jsonify(res)

@app.route('/api/auth/logout',methods= ["POST","GET"])
def logout():
    return jsonify(message="This is the logout of our API")



@app.route('/api/cars/<int:id>/favourite',methods= ["POST","GET"])
def addfavcar(id):
    unfav= request.json['unfav']
    user_id = request.json['user_id']
    check = Favourites.query.filter_by(car_id = id).all()
    check_id = Favourites.query.filter_by(user_id = user_id).all()

    fav = False

    if unfav == False:
        if check_id != None:
            for i in check_id:
                for x in check:
                    if x.car_id == i.car_id and x.user_id == i.user_id:
                        findunfav = Favourites.query.get_or_404(int(x.id))
                        db.session.delete(findunfav)
                        db.session.commit()
                        return jsonify(fav = False)


    carsschema = cars_schema()
    
    if check_id != None:
        for i in check_id:
            for x in check:
                if x.car_id == i.car_id and x.user_id == i.user_id:
                    return jsonify(fav = True)
    else:
        print("was here ")
                
    print("this is thes user id", user_id)
    cars =  Cars.query.filter_by(id = id).first()
    
    carss = carsschema.dump(cars)
    
    fav = Favourites(car_id = cars.id, user_id = user_id)
    db.session.add(fav)
    db.session.commit()

    return jsonify(message="This is the add to favourite of our API")   

@app.route('/api/search',methods= ["POST","GET"])
def search():
    form = SearchForm()
    carsschema = cars_schema(many = True)

    print("this isi the data", form.model.data)
    model = form.model.data
    make = form.make.data
    cars = []
    if make == '' and model == '':
        cars =  Cars.query.all()
        carss = carsschema.dump(cars)
        return jsonify(carss)
    elif make != '' and model == '':
        cars =  Cars.query.filter(Cars.make.like('%'+ make +'%')).all()
        carss = carsschema.dump(cars)
    elif make =='' and model != '':
        cars =  Cars.query.filter(Cars.model.like('%'+ model +'%')).all()
        carss = carsschema.dump(cars)
    elif make != '' and model != '':
        car_make= Cars.query.filter(Cars.make.like('%'+ make +'%')).all()
        car_model= Cars.query.filter(Cars.model.like('%'+ model +'%')).all()
        if car_make != None and car_model != None:
            for i in car_make:
                for x in car_model:
                    if x.model == i.model and x.make == i.make:
                            cars.append(Cars.query.get_or_404(int(x.id)))
        else:                    
            cars =  Cars.query.all()
        carss = carsschema.dump(cars)
        return jsonify(carss)
    return jsonify(carss)

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
@app.route('/api/image', methods=['GET'])
def get_image():
    return jsonify(send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), path = "Car.jpg"))


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