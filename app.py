from flask import Flask, render_template
from data import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sessions')
def handle_sessions():
    sessions = get_sessions()
    return render_template('sessions.html', sessions=sessions)

@app.route('/legislative_periods')
def handle_legislative_periods():
    periods = get_legislative_periods()
    return render_template('legislative_periods.html', periods=periods)

@app.route('/councillors')
@app.route('/councillors/<period>')
def handle_councillors(period=None):
    if not period:
        periods = get_legislative_periods()
        return render_template('councillors.html', periods=periods)
    else:
        councillors = get_councillors(period)
        return render_template('councillors_from_period.html', period=period, councillors=councillors)

@app.route('/councillor/<id>')
@app.route('/councillor/<period>/<id>')
def handle_councillor(id, period=None):
    councillor = get_councillor(id)
    return render_template('councillor.html', councillor=councillor, period=period)

@app.route('/votes/<councillor>')
def handle_votes(councillor):
    pass
