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
       (spit "/Users/heikofanieng/Documents/GitHub/nowplaying_rb_blt_udp/test/playlist.json" (str log-entry "\n") :append true)))))