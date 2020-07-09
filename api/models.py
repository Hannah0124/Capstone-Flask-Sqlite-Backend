from . import db

class Image(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image_url = db.Column(db.String)
  text = db.Column(db.String)
  translated_text = db.Column(db.Integer)
  favorite = db.Column(db.Boolean)