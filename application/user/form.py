from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
    
    username = StringField("Username", [validators.length(min=5)])
    password = StringField("Password", [validators.length(min=6)])
 
    class Meta:
        csrf = False
