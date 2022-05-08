from flask import render_template
from . import main



@main.route('/')
def index():
    title = 'Pitches'

    return render_template('index.html', title=title)

@main.route('/signup')
def signup():
    return render_template('signup.html')


@main.route('/signin')
def signin():
    return render_template('signin.html')