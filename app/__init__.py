import flask
from flask_socketio import SocketIO, send

from app.config import Config

app = flask.Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
app.config.from_object(Config)

from app import routes
