import socket
import json

# Funktion zum Empfangen von Daten über einen UDP-Socket

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

                # Zugriff auf den Wert von 'trackArtist' und Aktualisierung von 'interpret'
                interpret = json_data.get('trackArtist', '')

            except json.JSONDecodeError as e:
                print("Fehler beim Dekodieren der JSON-Daten:", e)

    finally:
        sock.close()  # Socket schließen

socket_receiver()