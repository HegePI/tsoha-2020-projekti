from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.length(min=5)])
    password = PasswordField("Password", [validators.length(min=6)])
  
    class Meta:
        csrf = False
