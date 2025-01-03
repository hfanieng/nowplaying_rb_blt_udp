(when trigger-active?
  (when (not= track-metadata (:last-track @locals))
    (swap! locals assoc :last-track track-metadata)
    (when (some? track-metadata)
      (let [payload {
      		"bpm"                effective-tempo
               "masterPlayerNumber" device-number
               "trackArtist"        track-artist
               "trackComment"       track-comment
               "trackKey"           track-key
               "trackGenre"         track-genre
               "trackLabel"         track-label
               "trackTitle"         track-title
               }]
        (send-json-to-webapp globals payload)))))
