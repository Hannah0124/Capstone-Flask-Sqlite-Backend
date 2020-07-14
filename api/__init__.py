from flask import Flask
from os import environ
from flask_sqlalchemy import SQLAlchemy

import os

from .commands import create_users, create_images, create_database
from .extensions import db, guard
from .models import User
from .routes import api

# db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

  # print("!!!")
  # print(app.config)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['SECRET_KEY'] = 'sdflkjweiofjwefijsldkjflsdfjk' #environ.get('SECRET_KEY')
  # app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nlmviczenkhkjl:6a2e77c6f597095382f1e070b66a82d08ea068c1cd95bce7729669813bbcdc29@ec2-50-17-90-177.compute-1.amazonaws.com:5432/dbanpqa83pbt1i'   
  # app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/mydb'
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