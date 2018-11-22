from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
  title=StringField('Pitch Title')
  content =TextAreaField('Project Pitch')
  author=TextAreaField('Your name as it\'ll be displayed')
  posted=TextAreaField('Date of upload')
  category=SelectField('Category', choices=[('business', 'Business'), ('tech', 'Technology'), ('sport', 'Sports'), ('pickup', 'pick up lines')])
  submit=SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio=StringField('Your Pitch Profile')
  submit=SubmitField('Submit')

class CommentForm(FlaskForm):
  comment=StringField('Your comment:')
  submit=SubmitField('Post')