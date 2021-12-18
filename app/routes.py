import flask
from flask_socketio import send

from app import app, socketio


@app.route('/')
def index():
    return flask.render_template("home.html")


@app.route('/activities')
def act():
    return flask.render_template("activities.html")


@app.route('/facts')
def fact():
    return flask.render_template("facts.html")


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


