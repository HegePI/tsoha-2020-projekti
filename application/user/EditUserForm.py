from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class EditUserForm(FlaskForm):
    
    username = StringField("Uusi käyttäjänimi", [validators.length(min=5)])
    password = PasswordField("Uusi salasana", [validators.length(min=6)])
 
    class Meta:
        csrf = False