from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Weather, Result
from application.forms import WeatherForm, ResultForm

@app.route('/', methods=['POST', 'GET'])
def index():
    weathers = Weather.query.all()
    results = Result.query.all()
    return render_template('index.html', weathers=weathers, results=results)
#will get database and display it on the webpage

@app.route('/addweather', methods=['POST', 'GET'])
def weatheradd():
    form = WeatherForm()
    if form.validate_on_submit():
        weathers = Weather(
            weather = form.weather.data, 
            timeofday = form.timeofday.data, 
            fk_rid = form.fk_rid.data
        )
        db.session.add(weathers) #code that adds it
        db.session.commit() #commit changes
        return redirect(url_for('index')) 
    return render_template('addweather.html', form=form ) #if the details have not been added it will return to this webpage

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def updateweather(id):
    form=WeatherForm()
    weathers= Weather.query.get(id)
    if form.validate_on_submit():
        weathers.weather = form.weather.data
        weathers.timeofday = form.timeofday.data
        weathers.fk_rid = form.fk_rid.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.weather.data = weathers.weather
        form.timeofday.data = weathers.timeofday
        form.fk_rid.data = weathers.fk_rid
    return render_template('updateweather.html', form=form) 

@app.route('/delete/<int:id>')
def deleteweather(id):
    weathers = Weather.query.get(id)
    db.session.delete(weathers)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/addresult', methods=['POST', 'GET'])
def resultadd():
    form = ResultForm()
    if form.validate_on_submit():
        results = Result(
            result = form.result.data
        )
        db.session.add(results) #code that adds it
        db.session.commit() #commit changes
        return redirect(url_for('index')) 
    return render_template('addresults.html', form=form )

@app.route('/updateresult/<int:rid>', methods=['GET', 'POST'])
def updateresult(rid):
    form=ResultForm()
    results= Result.query.get(rid)
    if form.validate_on_submit():
        results.result = form.result.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.result.data = results.result
    return render_template('updateresult.html', form=form) 

@app.route('/deleteresult/<int:rid>')
def deleteresult(rid):
    results = Result.query.get(rid)
    db.session.delete(results)
    db.session.commit()
    return redirect(url_for('index'))
