from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators

class NewUserForm(FlaskForm):
    
    username = StringField("Käyttäjänimi", [validators.length(min=5)])
    password = PasswordField("salasana", [validators.length(min=6)])
    admin = BooleanField("Admin")
 
    class Meta:
        csrf = False
