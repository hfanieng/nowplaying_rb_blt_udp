import http.server
import socketserver

# Definiere den Port, auf dem der Server laufen soll
PORT = 8000

# Erstelle einen Handler für HTTP-Anfragen
Handler = http.server.SimpleHTTPRequestHandler

# Erstelle einen TCP-Server, der auf dem angegebenen Port läuft
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    # Starte den Server, dieser läuft bis er manuell gestoppt wird
    httpd.serve_forever()