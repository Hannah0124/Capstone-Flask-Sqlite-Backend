from flask import Blueprint, jsonify, request
from . import db
from .models import User
from .models import Image

main = Blueprint('main', __name__)

@main.route('/add_user', methods=['POST'])
def add_user():
  # json - now a dictionary
  # take the data from require
  user_data = request.get_json()

  new_user = User(
    uid=user_data['uid'],
    provider=user_data['provider'],
    username=user_data['username'],
    email=user_data['email']
    )
  # adding to the database and commit
  db.session.add(new_user)
  db.session.commit()

  return 'Adding user', 201

@main.route('/saved_images')
def saved_images():

  images = []

  return jsonify({"images": images})