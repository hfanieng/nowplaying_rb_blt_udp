(when trigger-active?
  (when (not= track-metadata (:last-track @locals))
    (swap! locals assoc :last-track track-metadata)
    (when (some? track-metadata)
      (let [log-entry (json/write-str
                        {:timestamp (str (java.time.LocalDateTime/now))
                         :artist track-artist
                         :title track-title
                         :bpm effective-tempo}
                        :escape-slash false)]  ; optional, to control escaping slashes
       (send-json-to-webapp globals log-entry)))))
