(defn send-json-to-touchdesigner
  "Encodes a map as JSON and sends it in a UDP packet
  to TouchDesigner."
  [globals m]
  (let [message (str (cheshire.core/encode m) "\n")  ; Encode as JSON line.
       {:keys [td-address td-port td-socket]} @globals  ; Find where to send.
       data (.getBytes message)  ; Get JSON as raw byte array.
       packet (java.net.DatagramPacket. data (count data) td-address td-port)]
  (.send td-socket packet)))