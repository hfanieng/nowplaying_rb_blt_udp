import socket
import threading
import json
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

track_data = {}

# HTML-Template für die Anzeige der Track-Daten
html_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Track Information</title>
</head>
<body>
    <div>
        <h1>Track Information</h1>
        <p><strong>Track Title:</strong> {{ track_title }}</p>
        <p><strong>Artist:</strong> {{ track_artist }}</p>
        <p><strong>Genre:</strong> {{ track_genre }}</p>
        <p><strong>Key:</strong> {{ track_key }}</p>
        <p><strong>BPM:</strong> {{ bpm }}</p>
        <p><strong>Phrase Type:</strong> {{ phrase_type }}</p>
        <p><strong>Phrase Section:</strong> {{ phrase_section }}</p>
        <p><strong>Master Player Number:</strong> {{ master_player_number }}</p>
        <p><strong>Time Reached:</strong> {{ track_time_reached }}</p>
        <p><strong>Comment:</strong> {{ track_comment }}</p>
        <p><strong>Track Bank:</strong> {{ track_bank }}</p>
        <p><strong>Fill:</strong> {{ fill }}</p>
        <p><strong>Beat:</strong> {{ beat }}</p>
        <p><strong>Label:</strong> {{ track_label }}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, **track_data)

@app.route('/update', methods=['GET'])
def update():
    return jsonify(track_data)

def update_track_info(json_data):
    global track_data
    track_data = {
        "phrase_type": json_data.get("phraseType"),
        "track_key": json_data.get("trackKey"),
        "track_comment": json_data.get("trackComment"),
        "master_player_number": json_data.get("masterPlayerNumber"),
        "track_time_reached": json_data.get("trackTimereached"),
        "phrase_section": json_data.get("phraseSection"),
        "track_artist": json_data.get("trackArtist"),
        "track_genre": json_data.get("trackGenre"),
        "bpm": json_data.get("bpm"),
        "track_bank": json_data.get("trackBank"),
        "fill": json_data.get("fill"),
        "beat": json_data.get("beat"),
        "track_title": json_data.get("trackTitle"),
        "track_label": json_data.get("trackLabel")
    }

def socket_receiver():
    # Erstellen eines UDP-Sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 7000
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
    app.run(debug=True, use_reloader=False)