from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Review, Manager
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/survey', methods=['GET','POST'])
def survey():
    if request.method == 'POST':
        
        # requesting info from the user.html
        email = request.form.get('email')
        first_Name = request.form.get('first_Name')
        
        exsiting_Email = User.query.filter_by(email=email).first()
        if exsiting_Email:
            
            # creating a session so the info can be accessed in other pages
            session['User_email'] = email
            
            return redirect(url_for('views.question'))
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        else:
            # creating a query to input the info into the database
            new_user = User(email=email, first_Name=first_Name)
            
            # quering the database and adding the info
            db.session.add(new_user)
            db.session.commit()
        
        # directing the user to the questions.html if the info as been added correctly
        return redirect(url_for('views.question'))

    # directs the user to the same page if the request.method has an error
    return render_template("user.html")
    
@auth.route('/question', methods=['GET','POST'])
def question():
    if request.method == 'POST':
        if 'User_email' in session:
            
            # info requested from questions.html
            date = request.form.get('date')
            gender = request.form.get('gender')
            golf_Course = request.form.get('selection')
            golf_Rating = request.form.get('golf_rating')
            visit = request.form.get('visit')
            golf_ball = request.form.get('Gball')
            club = request.form.get('club')
            review_Rate = request.form.get('review_rating')
            add_Feedback = request.form.get('comment')
            
            # retreving the user info from previous page
            user_Email = session['User_email']
            
            # Creating the query for the Review table
            new_Review = Review(add_Feedback=add_Feedback, date=date, user_Email=user_Email, gender=gender, golf_Course=golf_Course, rating=golf_Rating, visits=visit, type_Golfball=golf_ball, club_Brand=club, review_Rate=review_Rate)
            
            # Adding query to the database
            db.session.add(new_Review)
            db.session.commit()
            
            # flashing a message that review was successfully submited
            flash('Review was Successfully Submited')
            
            # redirecting the user to a thank you page 
            return redirect(url_for('views.ty'))
        return render_template("questions.html")
    return render_template("questions.html")    

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/managementsignup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_Name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        golfCourse = request.form.get('selection')

        manager = Manager.query.filter_by(email=email).first()
        if manager:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_Name) < 2:
            flash('Name must be longer than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords must match, please check', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            new_manager = Manager(email=email, first_Name=first_Name, password=generate_password_hash(password1, method='sha256'), golf_Course=golfCourse)
            db.session.add(new_manager)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.login'))

    return render_template("management.html")

@auth.route('/managementlogin', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email') 
        password = request.form.get('password')

        manager = Manager.query.filter_by(email=email).first()
        if manager:
            if check_password_hash(manager.password, password):
                flash('Logged in successfully', category='success')
                return redirect(url_for('views.owner'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')
    return render_template("managementLogin.html")


