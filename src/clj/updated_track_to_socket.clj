(import '[java.net DatagramSocket DatagramPacket InetAddress])

(defn send-json-to-webapp
  "Encodes a map as JSON and sends it to the Astro web app."
  [globals m]
  (let [message (str (cheshire.core/encode m) "\n")  ; Encode as JSON line.
        {:keys [webapp-url]} @globals  ; Find where to send.
        response (clj-http.client/post webapp-url {:body message :content-type :json})]
    (println "Response from web app:" response)))

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
                        :escape-slash false)]
        (send-json-to-webapp globals log-entry)))))
