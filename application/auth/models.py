from application import db
from application.models import Base

from sqlalchemy.sql import text

class UserRoles(Base):
    __tablename__ = 'user_roles'
    account_id = db.Column(db.Integer(), db.ForeignKey('account.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

class Role(Base):
    name = db.Column(db.String(50), unique=True)

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False, unique=True)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)

    roles = db.relationship('Role', secondary='user_roles')

    games = db.relationship("Game", backref='account', lazy=True, cascade="delete")

    news = db.relationship("New", backref='account', lazy=True, cascade="delete")
  
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
    def get_roles(id):
        stmt = text("SELECT role.name"
                    " FROM account"
                    " INNER JOIN user_roles"
                    " ON user_roles.account_id = account.id"
                    " INNER JOIN role"
                    " ON role.id = user_roles.role_id"
                    " WHERE account.id = :id").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])

        return response 

    @staticmethod
    def find_users_with_no_games():
        stmt = text("SELECT Account.date_created, Account.username FROM Account"
                     " LEFT JOIN game_players ON game_players.account_id = Account.id"
                     " WHERE game_id IS NULL;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[1], "date_created":row[0]})

        return response

    @staticmethod
    def list_users_by_games_created(done=True):
        stmt = text("SELECT Account.id, Account.name, COUNT(*) FROM Account"
                " LEFT JOIN Game ON Game.account_id = Account.id"
                " WHERE (Game.done IS NOT null AND Game.done = :done)"
                " GROUP BY Account.id"
                " HAVING COUNT(Game.id) > 0"
                " ORDER BY COUNT(*) DESC").params(done=done)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[1], "games":row[2]})

        return response
    
    @staticmethod
    def list_users_by_games_played(done=True):
        stmt = text("SELECT Account.name, COUNT(*) FROM Account"
                " INNER JOIN game_players ON game_players.account_id = Account.id"
                " INNER JOIN Game ON Game.id = game_players.game_id"
                " WHERE Game.done = :done"
                " GROUP BY Account.id"
                " ORDER BY COUNT(*) DESC").params(done=done)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "games":row[1]})

        return response
    
    #SELECT Account.id, Account.name, COUNT(*) FROM Account INNER JOIN game_players ON game_players.account_id = Account.id INNER JOIN GAME ON Game.account_id = Account.id  WHERE (Game.done IS NOT null AND Game.done = True GROUP BY Account.id HAVING COUNT(Game.id) > 0 ORDER BY COUNT(*) DESC;
    #SELECT * FROM Account INNER JOIN game_players ON game_players.account_id = Account.id INNER JOIN Game ON Game.id = game_players.game_id WHERE Game.done = True;
    #SELECT Account.name, COUNT(*) FROM Account INNER JOIN game_players ON game_players.account_id = Account.id INNER JOIN Game ON Game.id = game_players.game_id WHERE Game.done = True GROUP BY Account.id;
    #SELECT Account.name, COUNT(*) FROM Account INNER JOIN game_players ON game_players.account_id = Account.id INNER JOIN Game ON Game.id = game_players.game_id WHERE Game.done = True GROUP BY Account.id ORDER BY COUNT(*) DESC;
    #SELECT Account.date_created, Account.username FROM Account LEFT JOIN game_players ON game_players.account_id = Account.id WHERE game_id IS NULL;