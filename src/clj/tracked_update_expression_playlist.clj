(when trigger-active?
  (when (not= track-metadata (:last-track @locals))
    (swap! locals assoc :last-track track-metadata)
    (when (some? track-metadata)
      (let [log-entry (with-out-str
                        (println "Timestamp:" (str (java.time.LocalDateTime/now)))
                        (println "   Artist:" track-artist)
                        (println "    Title:" track-title)
                        (println "      BPM:" effective-tempo)
                        (println))]
(spit "/Users/heikofanieng/Documents/GitHub/nowplaying_rb_blt_udp/test/playlist.txt" log-entry :append true)))))