from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class SignUpForm(FlaskForm):
    firstName = StringField("First name", [validators.Length(min=3, max=10)])
    lastName = StringField("Last name",[validators.Length(min=3, max=15)])
    username = StringField("Username", [validators.Length(min=3, max=15)])
    password = PasswordField("Password", [validators.Length(min=4, max=15)])

    class Meta:
        csrf = False