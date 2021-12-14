from app import app, socketio

if __name__ == "__main__":
    # app.run(port=5000, debug=True)
    socketio.run(app, debug=True)
    