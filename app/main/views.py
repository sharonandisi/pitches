from flask import render_template
from .import main

# Views
@main.route('/')
def index():
    title = 'Welcome to Pitches&Creme'
    return render_template('index.html',title=title, pitches=pitches)
if __name__ == '__main__':
    app.run(debug = True)

