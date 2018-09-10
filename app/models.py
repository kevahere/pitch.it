from . import db

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    password = db.Column(db.String(255))
    #Define relationship between user and pitch
    pitch = db.relationship('Pitch',backref = 'user',lazy = 'dynamic')

