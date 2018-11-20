from flask import render_template,request, redirect,url_for,abort
from ..models import Reviews, User
from .import main
from flask_login import login_required

# Views
@main.route('/')
def index():
    title = 'Welcome to Pitches&Creme'
    return render_template('index.html',title=title, pitches=pitches)
if __name__ == '__main__':
    app.run(debug = True)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

