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
  one = User(uid=123, provider="Google", username='One', password=guard.hash_password('one'))
  two = User(uid=456, provider="Google", username='Two', password=guard.hash_password('two'))
  three = User(uid=789, provider="Google", username='Three', password=guard.hash_password('three'))

  db.session.add_all([one, two, three])
  db.session.commit()


@click.command(name='create_images')
@with_appcontext
def create_images():
  one = Image(favorite=True, image_url="some image", language='Chinese', text="Happiness is beauty", translated_text="幸福实际上是我们里面的生活艺术", user_id=123)
  two = Image(favorite=True, image_url="some image 2", language='Korean', text="sloth", translated_text="나무늘보", user_id=123)
  three = Image(favorite=False, image_url="some image 3", language='Spanish', text="sky", translated_text="cielo", user_id=123)
  four = Image(favorite=True, image_url="some image 4", language='Korean', text="bear", translated_text="곰", user_id=456)

  db.session.add_all([one, two, three, four])
  db.session.commit()