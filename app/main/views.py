from flask import render_template
from . import main
# from .. import db,photos
from flask_login import login_required
from flask import render_template,request,redirect,abort
from .forms import UpdateProfile
from .. import db
from app.models import User




@main.route('/')
@login_required
def index():
    title = 'Pitches'

    return render_template('index.html', title=title)


@main.route('/users/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user=user)

@main.route('/users/<username>/update/pic', methods=['POST'])
def update_pic(username):
    user = User.query.filter(username=username).first()

    if 'photo' in request.file:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile.html',username=username))




@main.route('/users/<username>/update', methods=['GET','POST'])
# @login_required
def update_profile(username):
    user = User.query.filter(username=username).first()

    if user is None:
        abort(404)

    form = updateProfile()

    if form.validate_on_submit():
        user.bio =form.bio.data_files

        db.session.add(user)
        db.session.commit()


        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',form=form)