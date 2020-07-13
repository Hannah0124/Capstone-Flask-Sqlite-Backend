import click
from flask.cli import with_appcontext 

from .extensions import db, guard 
from .models import User, Image 

@click.command(name='create_database')
@with_appcontext
def create_database():
  db.create_all()

@click.command(name='create_users')
@with_appcontext
def create_users():
  one = User(uid="123", provider="Google", username='One', password=guard.hash_password('one'))
  two = User(uid="456", provider="Google", username='Two', password=guard.hash_password('two'))
  three = User(uid="789", provider="Google", username='Three', password=guard.hash_password('three'))

  db.session.add_all([one, two, three])
  db.session.commit()


@click.command(name='create_images')
@with_appcontext
def create_images():
  one = Image(favorite=True, image_url="https://images.unsplash.com/photo-1592168865720-df6eec2632d9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", language='Chinese', text="you are beautiful", translated_text="你是美麗的", user_id="123")
  two = Image(favorite=True, image_url="https://images.unsplash.com/photo-1489824904134-891ab64532f1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", language='Korean', text="car", translated_text="자동차", user_id="110807254680202631698")
  three = Image(favorite=True, image_url="https://images.unsplash.com/photo-1548266652-99cf27701ced?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", language='Spanish', text="sky", translated_text="cielo", user_id="123")
  four = Image(favorite=True, image_url="https://images.unsplash.com/photo-1589656966895-2f33e7653819?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", language='Korean', text="bear", translated_text="곰", user_id="123")
  five = Image(favorite=True, image_url="https://images.unsplash.com/photo-1563746870516-07dc33b40b92?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60", language='Korean', text="cactus", translated_text="선인장", user_id="110807254680202631698")

  db.session.add_all([one, two, three, four, five])
  db.session.commit()