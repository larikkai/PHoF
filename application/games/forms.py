from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators

class GameForm(FlaskForm):
    name = StringField("Game name", [validators.Length(min=5)])
    playerCount = IntegerField("Player count", [validators.NumberRange(min=2, max=4)])
    done = BooleanField("Done")
 
    class Meta:
        csrf = False