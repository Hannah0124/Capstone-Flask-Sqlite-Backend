from flask import Flask
from flask_sqlalchemy import flask_sqlalchemy

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

  return app