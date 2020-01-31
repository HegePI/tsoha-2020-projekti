from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.length(min=5)])
    password = PasswordField("Salasana", [validators.length(min=6)])
  
    class Meta:
        csrf = False
