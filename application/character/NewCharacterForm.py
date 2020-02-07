from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class NewCharacterForm(FlaskForm):
    
    character_name = StringField("Nimi")
    character_class = StringField("Hahmoluokka")
    character_race = StringField("Rotu")
    character_strength = IntegerField("Voima")
    character_dexterity = IntegerField("Hienomotoriikka")
    character_inteligence = IntegerField("Äly")
    character_faith = IntegerField("Usko")
    character_health = IntegerField("Elinvoima")
    character_mana = IntegerField("Mana")
 
    class Meta:
        csrf = False