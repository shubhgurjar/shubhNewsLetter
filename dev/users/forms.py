from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from dev.models import db_model

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = db_model.User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Input username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = db_model.User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Input email is taken. Please choose a different one.')
