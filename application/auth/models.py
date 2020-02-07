from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    games = db.relationship("Game", backref='account', lazy=True)
  
    def __init__(self, name):
        self.name = name
        
    def get_id(self):
        return self.id
  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_users_with_no_games(done=False):
        stmt = text("SELECT Account.id, Account.name FROM Account"
                     " LEFT JOIN Game ON Game.account_id = Account.id"
                     " WHERE (Game.done IS null OR Game.done = :done)"
                     " GROUP BY Account.id"
                     " HAVING COUNT(Game.id) = 0").params(done=done)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[1]})

        return response

    @staticmethod
    def list_users_by_games_played(done=True):
        stmt = text("SELECT Account.id, Account.name, COUNT(*) FROM Account"
                " LEFT JOIN Game ON Game.account_id = Account.id"
                " WHERE (Game.done NOT null AND Game.done = :done)"
                " GROUP BY Account.id"
                " HAVING COUNT(Game.id) > 0"
                " ORDER BY COUNT(*) DESC").params(done=done)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[1], "games":row[2]})

        return response