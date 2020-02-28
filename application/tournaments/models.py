from application import db
from application.models import Base

from sqlalchemy.sql import text

tournamentPlayers = db.Table('tournament_players', 
    db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('tournament_id', db.Integer, db.ForeignKey('tournament.id'))
)

tournamentGames = db.Table('tournament_games', 
    db.Column('tournament_id', db.Integer, db.ForeignKey('tournament.id')),
    db.Column('games_id', db.Integer, db.ForeignKey('game.id'))
)

class Tournament(Base):
    name = db.Column(db.String(144), nullable=False)
    playerCount =db.Column(db.Integer, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    
    players = db.relationship(
        'User', secondary=tournamentPlayers, backref='tournamentPlayers', lazy=True)

    games = db.relationship(
        'Game', secondary=tournamentGames, backref='tournamentGames', lazy=True, cascade="delete")

    def __init__(self, name):
        self.name = name
        self.done = False

    @staticmethod
    def find_how_many_players_in(tournamentid):
        stmt = text("SELECT COUNT(*) FROM Account"
                    " INNER JOIN tournament_players ON tournament_players.account_id = Account.id"
                    " LEFT JOIN Tournament ON Tournament.id = tournament_players.tournament_id"
                    " WHERE Tournament.id = :tournamentid").params(tournamentid=tournamentid)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"players":row[0]})

        return response
    
    @staticmethod
    def find_players_in_tournaments():
        stmt = text("SELECT Tournament.id, COUNT(*) FROM Tournament"
                    " INNER JOIN tournament_players ON tournament_players.tournament_id = Tournament.id"
                    " LEFT JOIN Account ON Account.id = tournament_players.account_id"
                    " GROUP BY Tournament.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"tournamentid":row[0], "players":row[1]})

        return response
    
    @staticmethod
    def find_players_in_single_tournament(tournamentid):
        stmt = text("SELECT * FROM Tournament"
                    " INNER JOIN tournament_players ON tournament_players.tournament_id = Tournament.id"
                    " LEFT JOIN Account ON Account.id = tournament_players.account_id"
                    " WHERE Tournament.id = :tournamentid").params(tournamentid=tournamentid)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[13]})

        return response
    
    @staticmethod
    def find_games_in_tournament(tournamentid):
        stmt = text("SELECT * FROM Game"
                    " INNER JOIN tournament_games ON tournament_games.games_id = Game.id"
                    " WHERE tournament_id = :tournamentid").params(tournamentid=tournamentid)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"tournamentname":row[3], "gameid":row[10]})

        return response