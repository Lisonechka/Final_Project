import flask
from flask_socketio import SocketIO

from app.config import Config

app = flask.Flask(__name__)
socketio = SocketIO(app)
app.config.from_object(Config)

from app import routes
