from application import db

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather = db.Column(db.String(80), nullable=False)
    timeofday = db.Column(db.String(12), nullable=False)
    fk_rid = db.Column(db.Integer, db.ForeignKey('result.rid'))

class Result(db.Model):
    rid = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(80), nullable=False)
