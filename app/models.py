from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from .import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
  __tablename__='users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  first_name = db.Column(db.String(255))
  surname = db.Column(db.String(255))
  bio = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
     @property
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

class Comment(db.Model):
     
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments
class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String)
    content = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_id = db.Column(db.Integer,db.ForeignKey("comments.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

class Category(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String)

    def save_category(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches

class Role(db.Model):
    __table__tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role', lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
    



