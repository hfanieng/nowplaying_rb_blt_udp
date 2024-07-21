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
(send-json-to-touchdesigner globals payload))