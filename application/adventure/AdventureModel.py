from application import db
from sqlalchemy.sql import text

class Adventure(db.Model):

    __tablename__ = "adventure"
    
    id = db.Column(db.Integer, primary_key=True)
    adventure_name = db.Column(db.String(120), nullable=False)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    ongoing = db.Column(db.Integer, nullable=False)
    dungeon_master = db.Column(db.Integer, db.ForeignKey('accounts.id'),nullable=False)
    

    def __init__(self, name, ongoing, dm):
        self.adventure_name = name
        self.ongoing = ongoing
        self.dungeon_master = dm

    @staticmethod
    def find_users_adventures(id):
        stmt = text("SELECT * FROM adventure WHERE (dungeon_master = %d);" % id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[1], "created":row[2]})

        return response

    @staticmethod
    def find_all_adventures():
        stmt = text("SELECT * FROM adventure;")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({ "id":row[0], "name":row[1], "created":row[2] })
        
        return response

    @staticmethod
    def find_adventure_by_id(id):
        stmt = text("SELECT * FROM adventure WHERE id = %d;" % id)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({ "id":row[0], "name":row[1], "created":row[2] })
        
        return response