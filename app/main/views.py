from flask import render_template
from . import main
from .. import db,photos
from flask_login import login_required
from flask import render_template,request,redirect,abort



@main.route('/')
@login_required
def index():
    title = 'Pitches'

    return render_template('index.html', title=title)


@main.route('/users/<username>')
@login_required
def profile(username):
    user = User.query.filter(username=username).first()

    if user is None:
        abort(404)

    return render_template('profile.html',username=user)

@main.route('/users/<username>/update/pic', methods=['POST'])
def update_pic(username):
    user = User.query.filter(username=username).first()

    if 'photo' in request.file:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile.html',username=username))