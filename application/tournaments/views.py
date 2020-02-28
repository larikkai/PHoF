from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
import random

from application import app, db
from application.tournaments.models import Tournament
from application.tournaments.forms import TournamentForm

from application.games.models import Game
from application.games.forms import GameForm
from application.games.views import games_create

from application.auth.models import User


@app.route("/tournaments/", methods=["GET"])
def tournaments_index():
    return render_template("tournaments/list.html", tournaments = Tournament.query.all(), playersInTournaments=Tournament.find_players_in_tournaments())

  
@app.route("/tournaments/new/")
@login_required
def tournaments_form():
    players = [2,4,8]
    return render_template("tournaments/new.html", players = players, form = TournamentForm())

@app.route("/tournaments/<tournament_id>/", methods=["GET"])
@login_required
def tournaments_view_tournament(tournament_id):

    tournament = Tournament.query.get(tournament_id)
    tournamentGames = Tournament.find_games_in_tournament(tournament_id)

    for game in tournamentGames:
        print(game)

    return render_template("tournaments/single.html", tournament = tournament, tournamentGames=tournamentGames)


@app.route("/tournaments/<tournament_id>/remove", methods=["POST"])
@login_required
def tournaments_remove(tournament_id):

    tournament = Tournament.query.get(tournament_id)
    db.session().delete(tournament)
    db.session().commit()
  
    return redirect(url_for("tournaments_index"))

@app.route("/tournaments/<tournament_id>/join", methods=["POST"])
@login_required
def tournaments_join(tournament_id):

    tournament = Tournament.query.get(tournament_id)
    
    user = User.query.get(current_user.id)
    tournament.players.append(user)

    if len(tournament.players) == tournament.playerCount:
        value = 0

        while value != tournament.playerCount:
            playersInRound = []
            game = Game(tournament.name)
            game.playerCount = 4
            game.done = False
            game.account_id = current_user.id
            playerCountValue = 0
            while playerCountValue != 4:
                randomPlayer = random.choice(tournament.players)
                if randomPlayer not in playersInRound and randomPlayer not in game.players:
                    game.players.append(randomPlayer)
                    playersInRound.append(randomPlayer)
                    playerCountValue += 1
            tournament.games.append(game)
  
            db.session().add(game)
            value+=1

    db.session().add(tournament)
    db.session().commit()
  
    return redirect(url_for("tournaments_index"))

@app.route("/tournaments/<tournament_id>/leave", methods=["POST"])
@login_required
def tournament_leave(tournament_id):

    tournament = Tournament.query.get(tournament_id)

    user = User.query.get(current_user.id)

    tournament.players.remove(user)

    db.session().add(tournament)
    db.session().commit()
  
    return redirect(url_for("tournaments_index"))

@app.route("/tournament/", methods=["POST"])
@login_required
def tournaments_create():
    form = TournamentForm(request.form)
  
    if not form.validate():
        return render_template("tournaments/new.html", form = form)
  
    tournament = Tournament(form.name.data)
    tournament.playerCount = form.playerCount.data
    tournament.done = False
    tournament.account_id = current_user.id

    user = User.query.get(current_user.id)
    tournament.players.append(user)
  
    db.session().add(tournament)
    db.session().commit()
  
    return redirect(url_for("tournaments_index"))