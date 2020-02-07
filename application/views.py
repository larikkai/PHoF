from flask import render_template
from application import app

from application.auth.models import User

@app.route('/')
def index():
    return render_template("index.html", needs_games=User.find_users_with_no_games(), list_games=User.list_users_by_games_played())