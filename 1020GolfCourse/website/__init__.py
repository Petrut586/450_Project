from pydoc import ModuleScanner
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "golfreview.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'GOLFCOURSEPROJECT'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    Bootstrap(app)
    datepicker(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from . import models 
                            # , Manager, User, Review

    with app.app_context():
        db.create_all()
    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.managementLogin'
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     return Manager.query.get(int(id))
        
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


