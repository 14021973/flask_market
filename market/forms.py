from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import length, equal_to, email, data_required, ValidationError

from market.models import Kzuser


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_chceck):
        user = Kzuser.query.filter_by(username=username_to_chceck.data).first()
        if user:
            raise ValidationError('Username already exists! Try another one !')

    def validate_email_address(self, email_address_to_chceck):
        email_address = Kzuser.query.filter_by(email_address=email_address_to_chceck.data).first()
        if email_address:
            raise ValidationError('Email address already exists! Try another one !')

    username = StringField(label='User Name:', validators=[length(min=3, max=30), data_required()])
    email_address = StringField(label='Email address:', validators=[email(), data_required()])
    password1 = PasswordField(label='Password:', validators=[length(min=6), data_required()])
    password2 = PasswordField(label='Confirm Password:', validators=[equal_to('password1'), data_required()])
    submit = SubmitField(label='Create account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[data_required()])
    password1 = PasswordField(label='Password:', validators=[data_required()])
    submit = SubmitField(label='Sign in')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')
