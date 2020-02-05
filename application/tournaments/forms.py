from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, validators, ValidationError

class TournamentForm(FlaskForm):

    def customValidation(self,field):
        if (field.data)%2 != 0:
            raise ValidationError('Number must be even')
    
    name = StringField("Tournament name", [validators.length(min=5)])
    playerCount = IntegerField("Player count", [validators.NumberRange(min=4, max=8), customValidation])
    done = BooleanField("Done")

    class Meta:
        csrf = False