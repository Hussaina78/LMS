from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField,TextAreaField, IntegerField,BooleanField,SelectField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,Regexp,Optional
from flask_login import current_user
from lms.models import User

#User Forms

class RegistrationForm(FlaskForm):
    name = StringField('Name', render_kw={'placeholder':'Name'}, validators=[DataRequired(), Length(1,100)])
    email = StringField('Email', render_kw={'placeholder':'Email'}, validators=[DataRequired(), Email()])
    email_preference = BooleanField('Do you want to receieve messages and all')
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


#Creating a registration form
class Registration(FlaskForm):
    name = StringField('Name', render_kw={'placeholder':'Name'}, validators=[DataRequired(), Length(1,100)])
    email = StringField('Email', render_kw={'placeholder':'Email'}, validators=[DataRequired(), Email()])
    email_preference = BooleanField('Do you want to receieve messages and all')
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class Login(FlaskForm):
   
    email = StringField('Email', render_kw={'placeholder':'Email'}, validators=[DataRequired(), Email()])
    rememberme = BooleanField('Keep me logged in? ')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class Logininstructor(FlaskForm):
   
    email = StringField('Email', render_kw={'placeholder':'Email'}, validators=[DataRequired(), Email()])
    rememberme = BooleanField('Keep me logged in? ')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class Registerinstructor(FlaskForm):
   
    email = StringField('Email', render_kw={'placeholder':'Email'}, validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('username', render_kw={'placeholder':'Enter username'}, validators=[DataRequired()])
    rememberme = BooleanField('Keep me logged in? ')
    
    submit = SubmitField('Sign Up')