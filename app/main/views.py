from . import main
from flask import render_template,request, redirect,url_for,abort, flash
from .. import db
from ..models import  User, Pitch , Comment
from flask_login import login_required, current_user
from .forms import PitchForm

#
@main.route('/')
@login_required
def index():
    pitches=Pitch.query.all()
    title = 'Welcome to Pitches&Creme'
    return render_template("index.html", title = title, pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id=user.id
    print(user_id)
    pitches = Pitch.query.filter_by(id=user_id).all()
    print(pitches)
    message='You don\'t have any pitches to show!'
    if not pitches:
        message='You don\'t have any pitches to show!'
        print(message)
    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user, pitches=pitches, message=message)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data 

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html')


@main.route('/writing-pitch', methods=['GET', 'POST'])
@login_required
def write_pitch():
    form = PitchForm()
    if form.validate_on_submit:
        pitch = Pitch(content=form.content.data, category=form.category.data, posted=form.posted.data)

        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))

    title = 'New Pitch'
    return render_template('new_pitch.html', pitch=form, title=title)


@main.route('/business')
def get_business():
    pitches = Pitch.query.filter_by(category='bus')
    title='Business'
    message='There are no pitches in the Business section.'
    if pitches is not 0:
        message='Home of Business pitches'
    return render_template('index.html', pitches=pitches, title=title, message=message)

@main.route('/sports')
def get_sports():
    pitches = Pitch.query.filter_by(category='spr')
    title='Sports'
    message='There are no pitches in the Sports section'
    if pitches is not 0:
        message='Home of Sports pitches'
    return render_template('index.html', pitches=pitches, title=title, message=message)

@main.route('/technology')
def get_technology():
  pitches = Pitch.query.filter_by(category='tech')
  title='Tech'
  message='There are no pitches in the Tech section'
  if pitches is not 0:
    message='Home of Tech pitches'
  return render_template('index.html', pitches=pitches, title=title, message=message)

@main.route('/pickup')
def get_misc():
  pitches = Pitch.query.filter_by(category='pickup')
  title='Pick up Lines'
  message='There are no pitches in the Pick up lines.'
  if pitches is not 0:
    message='Home of Misc. pitches'
  return render_template('index.html', pitches=pitches, title=title, message=message)

@main.route('/view-comments/<id>')
def view_comments(id):
  pitch = Pitch.query.filter_by(id=id)
  comments = Comments.query.filter_by(id=id)
  message='This pathetic pitch has no comments'
  if comments is not 0:
    message=f'You\'re now viewing the comments. Click home to continue browsing pitches'
  return render_template('comments.html', message=message, comments=comments, pitch=pitch)

@main.route('/delete/<id>')
def pitch_delete(id):
  pitch = Pitch.query.filter_by(id=id)
  return pitch.delete_pitch()




if __name__ == '__main__':
    app.run(debug = True)