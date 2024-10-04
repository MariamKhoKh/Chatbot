from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    email = StringField('Email', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$',
               message="Email must contain '@', a domain name, and a valid top-level domain (e.g., example.com).")
    ])

    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, max=20, message="Password must be between 8 and 20 characters."),
        Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', message="Password must contain both letters and numbers.")
    ])

    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, max=20, message="Password must be between 8 and 20 characters")
    ])
    submit = SubmitField('Log In')


class ChatForm(FlaskForm):
    user_input = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
