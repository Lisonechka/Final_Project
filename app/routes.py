import flask
from app import app


@app.route('/')
def index():
    return flask.render_template("home.html")
