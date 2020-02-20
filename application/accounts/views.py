from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db, adminlogin_required
from application.games.models import Game
from application.games.forms import GameForm
from application.games.forms import GameResultForm
from application.auth.models import User


@app.route("/users/", methods=["GET"])
def users_index():
    return render_template("users/list.html", users = User.query.all(),
        needs_games=User.find_users_with_no_games(), list_games=User.list_users_by_games_played())