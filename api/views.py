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

# should be nested routes? or save user in session ?
# example for nested route - "/api/movies/<int:movie_id>/cast_members" 
@main.route('/add_image')
def add_image():
  image_data = request.get_json()

  new_image = Image(
    words=image_data['words'],
    translatedWords=image_data['translatedWords'],
    photo_url=image_data['photo_url'],
    favorite=image_data['favorite'],
    user_id=image_data['user_id'] # should be pass as params
  )

  db.session.add(new_image)
  db.session.commit()

  return 'Adding image', 201