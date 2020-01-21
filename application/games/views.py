from application import app, db
from flask import redirect, render_template, request, url_for
from application.games.models import Game

@app.route("/games", methods=["GET"])
def games_index():
    return render_template("games/list.html", games = Game.query.all())

@app.route("/games/new/")
def games_form():
    return render_template("games/new.html")

@app.route("/games/<game_id>/", methods=["POST"])
def games_set_done(game_id):
    g = Game.query.get(game_id)

    g.done = True
    db.session().commit()
  
    return redirect(url_for("games_index"))

@app.route("/games/", methods=["POST"])
def games_create():
    g = Game(request.form.get("name"))

    db.session().add(g)
    db.session().commit()
  
    return redirect(url_for("games_index"))