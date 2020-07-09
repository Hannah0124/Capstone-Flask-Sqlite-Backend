from . import db

class Image(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image_uri = db.Column(db.String)
  text = db.Column(db.String)
  translated_text = db.Column(db.Integer)