from application import db
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship

class Adventure(db.Model):

    __tablename__ = "adventure"
    
    id = db.Column(db.Integer, primary_key=True)
    adventure_name = db.Column(db.String(120), nullable=False)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    ongoing = db.Column(db.Integer, nullable=False)
    dungeon_master = db.Column(db.Integer, db.ForeignKey('accounts.id'),nullable=False)
    character = relationship("Character", cascade="all, delete", backref="Adventure")
    

    def __init__(self, name, ongoing, dm):
        self.adventure_name = name
        self.ongoing = ongoing
        self.dungeon_master = dm
    
    @staticmethod
    def list_adventures():
        stmt = text("SELECT adventure.id, adventure.adventure_name, adventure.created, "
        "adventure.ongoing, accounts.username FROM adventure INNER JOIN "
        "accounts ON adventure.dungeon_master=accounts.id;")

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id":row[0], "adventure_name": row[1], "created": row[2],
            "ongoing": row[3], "dungeon_master": row[4]})

        return response