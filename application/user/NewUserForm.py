from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class NewUserForm(FlaskForm):
    
    username = StringField("Käyttäjänimi", [validators.length(min=5)])
    password = PasswordField("salasana", [validators.length(min=6)])
 
    class Meta:
        csrf = False
