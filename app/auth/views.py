from flask import flash, redirect, render_template, request,url_for
from . import auth
from ..models import User
from .. import db
from .forms import SignupForm,SigninForm
from flask_login import login_user,logout_user,login_required
from ..email import mail_message


@auth.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email = form.email.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message("Welcome to pitches","email/welcome_user",user.email,user=user)
       
        return redirect(url_for('auth.signin'))
        title = "New Account"

    return render_template('signup.html', Form=form)


@auth.route('signin', methods=['GET','POST'])
def signin():
    Form = SigninForm() 

    if Form.validate_on_submit():
        user = User.query.filter_by(email=Form.email.data).first()
        if user != None and user.verify_password(Form.password.data):
            login_user(user, Form.remember.data)

            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')

    title = "Pitches Signed in"

    return render_template('signin.html',Form=Form,title=title)


@auth.route('/logout')
@login_required
def signout():
    logout_user()
    return redirect(url_for("main.index")) 



    