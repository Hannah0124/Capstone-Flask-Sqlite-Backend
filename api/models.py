from . import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  uid = db.Column(db.Integer, unique=True, nullable=False)
  provider = db.Column(db.String) #default - Google?
  username = db.Column(db.String)
  email = db.Column(db.String)
  image = db.relationship('Image', backref='user', lazy=True )

class Image(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  words = db.Column(db.String)
  translatedWords = db.Column(db.String)
  photo_url = db.Column(db.String)
  favorite = db.Column(db.Boolean, default=False) #default - false? 
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)