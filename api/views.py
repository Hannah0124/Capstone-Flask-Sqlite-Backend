from flask import Blueprint, jsonify, request
from . import db 
from .models import Image

main = Blueprint('main', __name__)

# endpoint
@main.route('/add_image', methods=['POST'])

def add_image():
  image_data = request.get_json()

  # create new image object
  new_image = Image(image_uri=image_data['image_uri'], text=image_data['text'], translated_text=image_data['translated_text'])
  
  db.session.add(new_image)
  db.session.commit()


  return 'Done', 201  # success

# endpoint
@main.route('/images')

def images():
  image_list = Image.query.all()
  images = []

  for image in image_list:
    images.append({ 
      'image_uri': image.image_uri, 
      'text': image.text, 
      'translated_text': image.translated_text 
    })

  return jsonify({'images' : images})