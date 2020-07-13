# from . import db
from .extensions import db

class Image(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image_url = db.Column(db.String)
  text = db.Column(db.String, nullable=False)
  # text = db.Column(db.String, unique=True, nullable=False)
  translated_text = db.Column(db.Integer, nullable=False)
  favorite = db.Column(db.Boolean, default=False)
  language = db.Column(db.String, nullable=False)
  user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  uid = db.Column(db.Integer, unique=True, nullable=False)
  provider = db.Column(db.String)
  username = db.Column(db.String, unique=True, nullable=False)
  password = db.Column(db.Text)
  email = db.Column(db.String)
  images = db.relationship('Image', backref='user', lazy=True)

  @classmethod 
  def lookup(cls, username):
    return cls.query.filter_by(username=username).one_or_none()

  @classmethod 
  def identify(cls, id):
    return cls.query.filter_by(id=id).one_or_none()

  @property
  def rolenames(self):
    return []

  @property
  def identity(self):
    return self.id


# one to many relationship
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

