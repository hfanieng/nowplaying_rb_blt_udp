# Empfang des aktuellen Tracks nach Track-Updates über UDP und Anzeige in einer Webanwendung
# Receiving the current track after track updates via UDP and displaying it in a web application

import socket
import threading
import json
from flask import Flask, render_template, jsonifyx
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

track_data = {}

@app.route('/')
def index():
    return render_template('index_1.html', **track_data)

@app.route('/update', methods=['GET'])
def update():
    return jsonify(track_data)

def convert_time(milliseconds):
    seconds = milliseconds / 1000
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"

def update_track_info(json_data):
    global track_data
    track_data = {
        "timestamp": json_data.get("timestamp"),
        "track_key": json_data.get("key"),
        "track_comment": json_data.get("track_comment"),
        "device": json_data.get("device"),
        "track_artist": json_data.get("artist"),
        "track_genre": json_data.get("track_genre"),
        "bpm": round(json_data.get("bpm"), 2) if json_data.get("bpm") is not None else None,
        "track_title": json_data.get("title"),
        "track_label": json_data.get("label")
    }
    socketio.emit('update', track_data)

def socket_receiver():
    # Erstellen eines UDP-Sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 7001
    sock.bind(('', port))
    print("Socket verbunden mit Port", port)
    receiving = True

    try:
        while receiving:
            print('\nWarten auf eine Nachricht')
            data, address = sock.recvfrom(4096)
            print('Erhaltene {} Bytes von {}'.format(len(data), address))

            try:
                json_data = json.loads(data)  # Daten dekodieren
                print("JSON-Daten erfolgreich dekodiert:", json_data)
                update_track_info(json_data)
            except json.JSONDecodeError as e:
                print("Fehler beim Dekodieren der JSON-Daten:", e)
    finally:
        sock.close()  # Socket schließen

if __name__ == '__main__':
    receiver_thread = threading.Thread(target=socket_receiver)
    receiver_thread.start()
    socketio.run(app, debug=True, use_reloader=False)
