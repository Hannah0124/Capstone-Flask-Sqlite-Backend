  
from flask import Blueprint, jsonify, request
from . import db 
from .models import Image
from .models import User 

main = Blueprint('main', __name__)

# endpoint
@main.route('/add_image', methods=['POST'])

def add_image():
  image_data = request.get_json()

  # create new image object
  new_image = Image(
    image_url=image_data['image_url'], 
    text=image_data['text'], 
    translated_text=image_data['translated_text'], favorite=image_data['favorite'],
    language=image_data['language'],
    user_id=image_data['user_id']
  )
  
  db.session.add(new_image)
  db.session.commit()

  response = {
    'status': 'success',
    'result': 'Successfully added an image'
  }

  return jsonify(response), 201  # success


# endpoint
@main.route('/images/', methods=['GET'])

def images():
  image_list = Image.query.all()
  images = []

  for image in image_list:
    images.append({ 
      'id': image.id,
      'image_url': image.image_url, 
      'text': image.text, 
      'translated_text': image.translated_text,
      'favorite': image.favorite,
      'language': image.language,
      'user_id': image.user_id 
    })

  return jsonify({'images' : images})



# endpoint
@main.route('/image/<id>', methods=['POST'])

def delete_image(id):
  # image_data = request.get_json(id)

  # image_data = Data.query.get(id)

  image_data = Image.query.get(id)

  db.session.delete(image_data)
  db.session.commit()

  response = {
    'status': 'success',
    'result': 'Successfully deleted the image'
  }

  return jsonify(response), 201  # success


# endpoint
@main.route('/add_user', methods=['POST'])

def add_user():
  user_data = request.get_json()

  # create new user object
  new_user = User(
    uid=user_data['uid'], 
    provider=user_data['provider'], 
    username=user_data['username'], 
    email=user_data['email'],
    password=user_data['password']
  )
  
  db.session.add(new_user)
  db.session.commit()


  response = {
    'status': 'success',
    'result': 'Successfully added a user'
  }

  return jsonify(response), 201  # success


# endpoint (TEST: need to delete later)
@main.route('/users')

def users():
  user_list = User.query.all()
  users = []

  for user in user_list:
    users.append({ 
      'id': user.id,
      'uid': user.uid,
      'provider': user.provider,
      'username': user.username,
      'email': user.email,
      'password': user.password
    })

  return jsonify({'users' : users})

# jsonify: https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view

# delete-route: https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12