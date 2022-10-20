from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Review
from . import db 
auth = Blueprint('auth', __name__)

@auth.route('/survey', methods=['GET','POST'])
def survey():
    if request.method == 'POST':
        email = request.form.get('email')
        first_Name = request.form.get('first_Name')
        # date = request.form.get('date')
        new_user = User(email=email, first_Name=first_Name)
        # review_Date = Review(date = date)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('views.question'))

    return render_template("user.html")
    
@auth.route('/question', methods=['GET','POST'])
def question():
    if request.method == 'POST':
        id = request.form['id']
        gender = request.form.get('gender')
        golf_Course = request.form.get('selection')
        
        new_review = Review(gender=gender, golf_Course=golf_Course)
        
        db.session.add(new_review)
        db.session.commit()
        
        flash('Review was Successfully Submited')
        return redirect(url_for('views.home'))
    return render_template("questions.html")    

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/managementsignup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('Name must be longer than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords must match, please check', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters', category='error')
        else:
            flash('Account created!', category='success')
    return render_template("management.html")

@auth.route('/managementlogin', methods=['GET','POST'])
def login():
    data = request.form
    return render_template("managementLogin.html")


