from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/add_user', methods=['POST'])
def add_user():

  return 'Adding user', 201