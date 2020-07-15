from flask import Flask
from os import environ
from flask_sqlalchemy import SQLAlchemy

import os

from .commands import create_users, create_images, create_database, delete_database
from .extensions import db, guard
from .models import User
from .routes import api

def create_app():
  app = Flask(__name__)

  # print(app.config)

  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SECRET_KEY'] = 'sdflkjweiofjwefijsldkjflsdfjk' 
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jljnpbloyqfwvn:813f849eaa918b21b8bd9c76e8be1bc01bb6c98b2605617fea25be3371965d74@ec2-34-239-241-25.compute-1.amazonaws.com:5432/d3are692suf1kb'  
  # 'sqlite:///database.db'
  app.config['JWT_ACCESS_LIFESPAN'] = {'minutes' : 1}

  # They way below is not working (TODO)
  # app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
  # app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI') 


  db.init_app(app)
  guard.init_app(app, User)

  app.cli.add_command(create_users)
  app.cli.add_command(create_images)
  app.cli.add_command(create_database)
  app.cli.add_command(delete_database)

  app.register_blueprint(api)

  from .views import main
  app.register_blueprint(main)

  return app