import email
from unicodedata import name
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators,SubmitField
from ..models import User


class SignupForm(FlaskForm):
    username = StringField('Enter your username',[validators.DataRequired()])
    email = StringField('Enter your email address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password',[validators.DataRequired(), validators.EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',[validators.DataRequired()])
    submit = SubmitField('Sign Up')
    

class SigninForm(FlaskForm):
    email = StringField('Enter your email address',[validators.DataRequired()])
    password = PasswordField('Password',[validators.DataRequired(), validators.EqualTo('password')])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')