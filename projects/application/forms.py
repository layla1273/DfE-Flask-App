from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from application.models import Weather

class WeatherForm(FlaskForm):
    weather = StringField("Weather")
    timeofday = StringField("timeofday")
    fk_rid = IntegerField("resultid")
    submit = SubmitField("submit") #allows us to enter a submit button for the database

class ResultForm(FlaskForm):
    result = StringField("result")
    submit = SubmitField("submit")
