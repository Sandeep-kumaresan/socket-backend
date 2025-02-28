from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def index():
    return "WebSocket Server Running!"

@socketio.on("connect")
def handle_connect():
    print("Client connected")
    emit("message", {"data": "Connected to WebSocket Server!"})

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")

@socketio.on("message")
def handle_message(data):
    print(f"Received: {data}")
    emit("message", f"Echo: {data}", broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

