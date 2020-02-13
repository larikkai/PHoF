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
                           nullable=False)
    
    players = db.relationship(
        'User', secondary=gamePlayers, backref='gamePlayers', lazy=True)
    

    def __init__(self, name):
        self.name = name
        #self.playerCount = 2
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