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

@app.route('/votes/affairs')
@app.route('/votes/affairs/<period>')
@app.route('/votes/affairs/<period>/page/<page>')
@app.route('/votes/affairs/<period>/<id>')
def handle_votes_affairs(period=None, id=None, page=1):
    if not period:
        periods = get_legislative_periods()
        return render_template('votes_affairs.html', periods=periods)
    elif not id:
        affairs = get_votes_affairs(period, page)
        return render_template('votes_affairs_per_period.html', period=period, page=page, affairs=affairs)
    else:
        affair = get_votes_affair(id)
        return render_template('votes_affair.html', period=period, affair=affair)

@app.route('/affairs/<period>/<id>')
def handle_affair(period, id):
    affair = get_affair(id)
    return render_template('affair.html', affair=affair)

@app.route('/votes/councillors/<period>/<id>')
@app.route('/votes/councillors/<period>/<id>/<page>')
def handle_votes_councillors(period, id, page=1):
    votes = get_votes_councillor(id, page)
    return render_template('votes_councillor.html', period=period, id=id, page=page, votes=votes)

@app.route('/viz')
def viz():
    return render_template('viz.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')