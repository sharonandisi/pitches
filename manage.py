from app import create_app, db
from app.models import User, Comments, Pitch

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Comments = Comments, Pitch = Pitch)
if __name__ == '__main__':
    manager.run()