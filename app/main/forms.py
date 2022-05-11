from flask_wtf import FlaskForm
from wtforms import Form, TextAreaField, validators,SubmitField
import email_validator



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',[validators.DataRequired()])
    submit = SubmitField('Submit')