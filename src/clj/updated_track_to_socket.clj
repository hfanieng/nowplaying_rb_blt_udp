(import '[java.net DatagramSocket DatagramPacket InetAddress])

(defn send-udp [host port message]
  (let [socket (DatagramSocket.)
        address (InetAddress/getByName host)
        buffer (.getBytes message)
        packet (DatagramPacket. buffer (count buffer) address port)]
    (.send socket packet)
    (.close socket)))

(when trigger-active?
  (when (not= track-metadata (:last-track @locals))
    (swap! locals assoc :last-track track-metadata)
    (when (some? track-metadata)
      (let [log-entry (json/write-str
                        {:timestamp (str (java.time.LocalDateTime/now))
					:device device-name
                         :artist track-artist
					:id rekordbox-id
                         :title track-title
                         :bpm effective-tempo}
                        :escape-slash false)
            udp-host "127.0.0.1"  ; Ziel-Host
            udp-port 7001]       ; Ziel-Port
        (send-udp udp-host udp-port log-entry)))))