from application import db
from application.models import Base

from sqlalchemy.sql import text

gamePlayers = db.Table('game_players', 
    db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)

class Game(Base):
    name = db.Column(db.String(144), nullable=False)
    playerCount = db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    score1 = db.Column(db.Integer)
    score2 = db.Column(db.Integer)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                        index=True)
    
    players = db.relationship(
        'User', secondary=gamePlayers, backref='gamePlayers', lazy=True)
    

    def __init__(self, name):
        self.name = name
        self.done = False

    @staticmethod
    def setScore(gameid, a, b):
        stmt = text("UPDATE game"
                    " SET score1 = a, score2 = b"
                    " WHERE Game_id = :gameid").params(gameid=gameid, a=a, b=b)
        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append(row[1])

        return response
    
    @staticmethod
    def find_how_many_players_in(gameid):
        stmt = text("SELECT COUNT(*) FROM Account"
                    " INNER JOIN game_players ON game_players.account_id = Account.id"
                    " LEFT JOIN Game ON Game.id = game_players.game_id"
                    " WHERE Game.id = :gameid").params(gameid=gameid)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"players":row[0]})

        return response
    
    @staticmethod
    def find_players_in_games():
        stmt = text("SELECT Game.id, COUNT(*) FROM Game"
                    " INNER JOIN game_players ON game_players.game_id = Game.id"
                    " LEFT JOIN Account ON Account.id = game_players.account_id"
                    " GROUP BY Game.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"gameid":row[0], "players":row[1]})

        return response

    @staticmethod
    def find_players_in_single_game(gameid):
        stmt = text("SELECT * FROM Game"
                    " INNER JOIN game_players ON game_players.game_id = Game.id"
                    " LEFT JOIN Account ON Account.id = game_players.account_id"
                    " WHERE Game.id = :gameid").params(gameid=gameid)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[9])

        return response

        #SELECT * FROM Game INNER JOIN game_players ON game_players.game_id = Game.id LEFT JOIN Account ON Account.id = game_players.account_id;
        #SELECT Game.id, COUNT(*) FROM Game INNER JOIN game_players ON game_players.game_id = Game.id LEFT JOIN Account ON Account.id = game_players.account_id GROUP BY Game.id;
        #SELECT COUNT(*) FROM Account INNER JOIN game_players ON game_players.account_id = Account.id LEFT JOIN Game ON Game.id = game_players.game_id WHERE Game.id = 1;