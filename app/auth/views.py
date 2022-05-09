from flask import render_template
from . import auth
from flask_login import login_required


@auth.route('/signin', methods=['GET','POST'])
@login_required
def signin():
    return render_template('auth/signin.html')
