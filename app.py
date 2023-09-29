# app.py

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    user = data['user']
    message = data['message']
    emit('receive_message', {'user': user, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)