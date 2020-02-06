from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewAdventureForm(FlaskForm):
    
    adventure_name = StringField("Seikkailun nimi", [validators.length(min=5)])
 
    class Meta:
        csrf = False