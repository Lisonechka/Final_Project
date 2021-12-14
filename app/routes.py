import flask
from app import app


@app.route('/')
def index():
    return flask.render_template("home.html")


@app.route('/activities')
def act():
    return flask.render_template("activities.html")


@app.route('/facts')
def fact():
    return flask.render_template("facts.html")
