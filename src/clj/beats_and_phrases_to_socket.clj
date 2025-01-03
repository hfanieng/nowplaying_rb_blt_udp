(let [payload {"beat"               beat-within-bar
			"beatNumber"		 beat-number
               "bpm"                effective-tempo
               "phraseSection"      section
               "phraseType"         phrase-type
               "masterPlayerNumber" device-number
               "trackArtist"        track-artist
               "trackBank"          track-bank
               "trackComment"       track-comment
               "trackDevice"		 device-name
               "trackKey"           track-key
               "trackGenre"         track-genre
               "trackLabel"         track-label
               "trackTimereached"   track-time-reached
               "trackTitle"         track-title
			"fill"               (= section :fill)}]
(send-json-to-webapp globals payload))

(defn send-json-to-webapp
  "Encodes a map as JSON and sends it to the Astro web app."
  [globals m]
  (let [message (str (cheshire.core/encode m) "\n")  ; Encode as JSON line.
        {:keys [webapp-url]} @globals  ; Find where to send.
        response (clj-http.client/post webapp-url {:body message :content-type :json})]
    (println "Response from web app:" response)))
