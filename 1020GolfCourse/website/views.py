from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
    
@views.route('/survey')
def survey():
    return render_template("user.html")

@views.route('/managementsignup')
def signup():
    return render_template("management.html")

@views.route('/managementlogin')
def login():
    return render_template("managementLogin.html")

@views.route('/thankyou')
def ty():
    return render_template("ty.html")

@views.route('/question')
def question():
    return render_template("questions.html")