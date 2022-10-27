from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Manager(db.Model, UserMixin):  
    id = db.Column(db.Integer, primary_key=True)
    first_Name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    golf_Course = db.Column(db.String(50))

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    add_Feedback = db.Column(db.String(10000))
    date = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    gender = db.Column(db.String(20))
    golf_Course = db.Column(db.String(50), db.ForeignKey('manager.golf_Course'))
    rating = db.Column(db.Integer)
    visits = db.Column(db.String(50))
    type_Golfball = db.Column(db.String(50))
    club_Brand = db.Column(db.String(50))
    review_Rate = db.Column(db.Integer)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_Name = db.Column(db.String(150))
    
   

