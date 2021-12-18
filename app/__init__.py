import flask
from flask_socketio import SocketIO, send

from app.config import Config

app = flask.Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app, cors_allowed_origins='*')

from app import routes
