;; Create a socket for sending UDP to TouchDesigner, and record the
;; address and port to which such UDP messages should be sent.
(swap! globals assoc :td-socket (java.net.DatagramSocket.))
(swap! globals assoc :td-address (java.net.InetAddress/getLocalHost))
(swap! globals assoc :td-port 7000)