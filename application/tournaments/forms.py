from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class TournamentForm(FlaskForm):
    name = StringField("Tournament name", [validators.length(min=5)])
    playerCount = IntegerField("Player count", [validators.NumberRange(min=2, max=64)])
    done = BooleanField("Done")

    class Meta:
        csrf = False