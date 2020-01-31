from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class SignUpForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password")

    class Meta:
        csrf = False