from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db, adminlogin_required
from application.games.models import Game
from application.games.forms import GameForm
from application.games.forms import GameResultForm
from application.auth.models import User


@app.route("/games/", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = Game.query.all(), playersInGames=Game.find_players_in_games())

@app.route("/games/new/")
@login_required
def games_form():
    return render_template("games/new.html", form = GameForm())

@app.route("/games/<game_id>/done", methods=["POST"])
@login_required
def games_set_done(game_id):

    game = Game.query.get(game_id)
    game.done = not game.done
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/<game_id>/score", methods=["POST"])
@login_required
def games_set_score(game_id):

    form = GameResultForm(request.form)

    game = Game.query.get(game_id)
    game.done = True
    game.score1 = form.score1.data
    game.score2 = form.score2.data
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/<game_id>", methods=["POST"])
@login_required
def games_join(game_id):

    game = Game.query.get(game_id)
    
    user = User.query.get(current_user.id)
    game.players.append(user)

    db.session().add(game)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/<game_id>/", methods=["GET"])
@login_required
def games_view_game(game_id):

    form = GameResultForm()
    game = Game.query.get(game_id)
    games = Game.query.all()

    return render_template("games/single.html", game = game, form = form, games=games)


@app.route("/games/<game_id>/remove", methods=["POST"])
@adminlogin_required(role='Admin')
def games_remove(game_id):

    game = Game.query.get(game_id)
    db.session().delete(game)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/<game_id>/leave", methods=["POST"])
@login_required
def game_leave(game_id):

    game = Game.query.get(game_id)

    user = User.query.get(current_user.id)

    game.players.remove(user)

    db.session().add(game)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/", methods=["POST"])
@login_required
def games_create():

    form = GameForm(request.form)
  
    if not form.validate():
        return render_template("games/new.html", form = form)
  
    game = Game(form.name.data)
    game.playerCount = form.playerCount.data
    game.done = False
    game.account_id = current_user.id

    user = User.query.get(current_user.id)
    game.players.append(user)
  
    db.session().add(game)
    db.session().commit()
  
    return redirect(url_for("games_index"))