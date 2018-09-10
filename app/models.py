from . import db

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    password = db.Column(db.String(255))
    #Define relationship between user and pitch
    pitch = db.relationship('Pitch',backref = 'user',lazy = 'dynamic')

    def __repr__(self):
        return f'User{self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id =  db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    pitch_body = db.Column(db.String)
    #Define the relationship between a User and a pitch
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def __repr__(self):
        return f'Pitch {self.title}'