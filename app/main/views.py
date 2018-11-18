from flask import render_template
from app import app

# Views
@main.route('/')
def index():
    title = 'Welcome to Pitches&Creme'
    return render_template('index.html',title=title, pitches=pitches)
    
