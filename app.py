from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import eventlet

eventlet.monkey_patch()  # Ensure eventlet works correctly

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")

@app.route('/')
def index():
    return "Flask WebSockets App Running on Azure!"

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit("server_message", "Welcome! You are connected.")

@socketio.on('message')
def handle_message(msg):
    print(f"Received: {msg}")
    emit("server_message", f"Echo: {msg}", broadcast=True)

@socketio.on('custom_event')
def handle_custom_event(data):
    print(f"Received custom event: {data}")
    emit("server_response", {"message": f"Server received: {data}"}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000)
