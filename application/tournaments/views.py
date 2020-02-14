from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tournaments.models import Tournament
from application.tournaments.forms import TournamentForm

from application.games.models import Game
from application.games.forms import GameForm
from application.games.views import games_create


@app.route("/tournaments/", methods=["GET"])
def tournaments_index():
    return render_template("tournaments/list.html", tournaments = Tournament.query.all())

  
@app.route("/tournaments/new/")
@login_required
def tournaments_form():
    players = [2,4,8]
    return render_template("tournaments/new.html", players = players, form = TournamentForm())

@app.route("/tournaments/<tournament_id>", methods=["POST"])
@login_required
def tournaments_set_done(tournament_id):

    tournament = Tournament.query.get(tournament_id)
    tournament.done = not tournament.done
    db.session().commit()
  
    return redirect(url_for("tournaments_index"))

@app.route("/tournaments/<tournament_id>/", methods=["GET"])
@login_required
def tournaments_view_tournament(tournament_id):
    return render_template("tournaments/single.html", tournament = Tournament.query.get(tournament_id))


@app.route("/tournaments/<tournament_id>/remove", methods=["POST"])
@login_required
def tournaments_remove(tournament_id):

    tournament = Tournament.query.get(tournament_id)
    db.session().delete(tournament)
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

    value = 0

    while value != tournament.playerCount:
        game = Game(form.name.data)
        game.playerCount = tournament.playerCount
        game.done = False
        game.account_id = current_user.id
  
        db.session().add(game)
        db.session().commit()
        value+=1
        

    tournament.done = form.done.data
    tournament.account_id = current_user.id
  
    db.session().add(tournament)
    db.session().commit()
  
    return redirect(url_for("tournaments_index"))