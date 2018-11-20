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
  pass_secure = db.Column(db.String(255))
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



