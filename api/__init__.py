from flask import Flask
from os import environ
from flask_sqlalchemy import SQLAlchemy

from .commands import create_users, create_images, create_database
from .extensions import db, guard
from .models import User
from .routes import api

# db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

  # print("!!!")
  # print(app.config)

  app.config['SECRET_KEY'] = 'sdflkjweiofjwefijsldkjflsdfjk' #environ.get('SECRET_KEY')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' #  
  app.config['JWT_ACCESS_LIFESPAN'] = {'minutes' : 1}

  # They way below is not working (TODO)
  # app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
  # app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI') 


  db.init_app(app)
  guard.init_app(app, User)

  app.cli.add_command(create_users)
  app.cli.add_command(create_images)
  app.cli.add_command(create_database)

  app.register_blueprint(api)

  from .views import main
  app.register_blueprint(main)

  return app

def getApp():
    return app