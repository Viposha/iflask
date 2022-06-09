from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign up')

	# def validate_username(self, field):
	# 	if User.query.filter_by(username=field.data).first():
	# 		raise ValidationError('Username already in use.')
	#
	# def validate_email(self, field):
	# 	if User.query.filter_by(email=field.data).first():
	# 		raise ValidationError('Email already registered.')


class LoginForm(FlaskForm):
	email = EmailField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')