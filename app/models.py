from . import db

class User(UserMixin, db.Model):
  __tablename__='users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  first_name = db.Column(db.String(255))
  surname = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))

  comments = db.relationship('Comments', backref='comments', lazy='dynamic')
  pitch = db.relationship('Pitch', backref='pitch', lazy='dynamic')

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )
if __name__ == '__main__':
    manager.run()
