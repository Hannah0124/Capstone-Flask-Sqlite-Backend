from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route('/add_user', methods=['POST'])
def add_user():

  return 'Adding user', 201

@main.route('/saved_images')
def saved_images():

  images = []

  return jsonify({"images": images})