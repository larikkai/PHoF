from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db, adminlogin_required
from application.games.models import Game
from application.games.forms import GameForm
from application.games.forms import GameResultForm
from application.auth.models import User


@app.route("/games/", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = Game.query.all())

  
@app.route("/games/new/")
@login_required
def games_form():
    return render_template("games/new.html", form = GameForm())

@app.route("/games/<game_id>/done", methods=["POST"])
@login_required
def games_set_done(game_id):

    g = Game.query.get(game_id)
    g.done = not g.done
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/<game_id>/score", methods=["POST"])
@login_required
def games_set_score(game_id):

    form = GameResultForm(request.form)

    g = Game.query.get(game_id)
    g.done = True
    g.score1 = form.score1.data
    g.score2 = form.score2.data
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/<game_id>", methods=["POST"])
@login_required
def games_join(game_id):

    g = Game.query.get(game_id)
    
    u = User.query.get(current_user.id)
    g.players.append(u)

    db.session().add(g)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/<game_id>/", methods=["GET"])
@login_required
def games_view_game(game_id):
    return render_template("games/single.html", game = Game.query.get(game_id), form=GameResultForm(), games=Game.query.all())


@app.route("/games/<game_id>/remove", methods=["POST"])
@adminlogin_required(role='Admin')
def games_remove(game_id):

    g = Game.query.get(game_id)
    db.session().delete(g)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/<game_id>/leave", methods=["POST"])
@adminlogin_required(role='Admin')
def game_leave(game_id):

    g = Game.query.get(game_id)

    u = User.query.get(current_user.id)

    g.players.remove(u)

    db.session().add(g)
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/", methods=["POST"])
@login_required
def games_create():
    form = GameForm(request.form)
  
    if not form.validate():
        return render_template("games/new.html", form = form)
  
    g = Game(form.name.data)
    g.playerCount = form.playerCount.data
    g.done = form.done.data
    g.account_id = current_user.id

    u = User.query.get(current_user.id)
    g.players.append(u)
  
    db.session().add(g)
    db.session().commit()
  
    return redirect(url_for("games_index"))