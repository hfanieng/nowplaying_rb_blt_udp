;; Create a socket for sending UDP to TouchDesigner, and record the
;; address and port to which such UDP messages should be sent.
(swap! globals assoc :td-socket (java.net.DatagramSocket.))
(swap! globals assoc :td-address (java.net.InetAddress/getLocalHost))
(swap! globals assoc :td-port 7000)

;; Create a socket for sending UDP to Python, and record the
;; address and port to which such UDP messages should be sent.
(swap! globals assoc :py-socket (java.net.DatagramSocket.))
(swap! globals assoc :py-address (java.net.InetAddress/getLocalHost))
(swap! globals assoc :py-port 7001)

;; Add a new setup for sending data to the Astro web app
(swap! globals assoc :webapp-url "http://localhost:3000/api/track")
