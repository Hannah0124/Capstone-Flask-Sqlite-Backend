import click
from flask.cli import with_appcontext 

from .extensions import db, guard 
from .models import User 

@click.command(name='create_database')
@with_appcontext
def create_database():
  db.create_all()

@click.command(name='create_users')
@with_appcontext
def create_users():
  one = User(uid=123, provider="Google", username='One', password=guard.hash_password('one'))
  two = User(uid=456, provider="Google", username='Two', password=guard.hash_password('two'))
  three = User(uid=789, provider="Google", username='Three', password=guard.hash_password('three'))

  db.session.add_all([one, two, three])
  db.session.commit()