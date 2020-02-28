from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class TournamentForm(FlaskForm):
    name = StringField("Tournament name", [validators.length(min=5, max=15)])
    playerCount = IntegerField("Player count", [validators.NumberRange(min=4, max=16)])
    done = BooleanField("Done")

    class Meta:
        csrf = False