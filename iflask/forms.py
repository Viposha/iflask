from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from iflask.models import User
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField, TextAreaField, FileField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
	email = EmailField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')


class CreatePostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	description = TextAreaField('Description', validators=[DataRequired()])
	picture = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Post')


class UploadAvatarForm(FlaskForm):
	picture = FileField('Upload Image', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Post')



