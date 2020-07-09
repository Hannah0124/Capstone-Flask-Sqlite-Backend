from . import db

class Image(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image_url = db.Column(db.String, unique=True)
  text = db.Column(db.String, unique=True, nullable=False)
  translated_text = db.Column(db.Integer, unique=True, nullable=False)
  favorite = db.Column(db.Boolean, default=False)
  language = db.Column(db.String, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  uid = db.Column(db.Integer, unique=True, nullable=False )
  provider = db.Column(db.String)
  username = db.Column(db.String, unique=True, nullable=False )
  email = db.Column(db.String)
  images = db.relationship('Image', backref='user', lazy=True)


# one to many relationship
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

