from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class GameForm(FlaskForm):
    name = StringField("Game name", [validators.Length(min=5, max=15)])
    playerCount = IntegerField("Player count", [validators.NumberRange(min=2, max=4)])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False

class GameResultForm(FlaskForm):
    score1 = IntegerField("Score 1", [validators.number_range(min=0, max=6)])
    score2 = IntegerField("Score 2", [validators.number_range(min=0, max=6)])
 
    class Meta:
        csrf = False