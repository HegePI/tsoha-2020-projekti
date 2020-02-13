from application import db
from sqlalchemy.sql import text

class Character(db.Model):

    __tablename__ = "character"
    
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(120), nullable=False)
    character_class = db.Column(db.String(120), nullable=False)
    character_race = db.Column(db.String(120), nullable=False)
    character_strength = db.Column(db.Integer)
    character_dexterity = db.Column(db.Integer)
    character_inteligence = db.Column(db.Integer) 
    character_faith = db.Column(db.Integer)
    character_health= db.Column(db.Integer)
    character_mana = db.Column(db.Integer)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'),nullable=False)
    adventure_id = db.Column(db.Integer, db.ForeignKey('adventure.id'),nullable=False)

    def __init__(self, c_name, c_class, c_race, c_strength, c_dexterity, c_inteligence, c_faith, c_health, c_mana, account_id, adventure_id):
        self.character_name = c_name
        self.character_class = c_class
        self.character_race = c_race
        self.character_strength = c_strength
        self.character_dexterity = c_dexterity
        self.character_inteligence = c_inteligence
        self.character_faith = c_faith
        self.character_health = c_health
        self.character_mana = c_mana
        self.account_id = account_id
        self.adventure_id = adventure_id

    @staticmethod
    def find_users_characters(user_id):
        stmt = text("SELECT * FROM character WHERE (account_id = %d);" % user_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"name":row[1], "class":row[2], "race":row[3], 
            "str":row[4], "dex":row[5], "int":row[6], "faith":row[7], "HP":row[8], "MP":row[9] })

        return response
    
    @staticmethod
    def find_all_characters():
        stmt = text("SELECT character.character_name, character.character_race, "
        "character.character_class, accounts.username, adventure.adventure_name "
        "FROM character INNER JOIN accounts ON character.account_id=accounts.id "
        "INNER JOIN adventure ON character.adventure_id=adventure.id;")

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"char_name":row[0], "char_race":row[1],
            "char_class":row[2], "username":row[3], "adventure_name":row[4]})

        return response


