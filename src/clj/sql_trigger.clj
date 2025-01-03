(require '[clojure.data.jdbc :as jdbc])  

(def db-spec {:subprotocol "mysql"
              :subname "//localhost:3306/v078803"
              :user "v078803"
              :password "HibaIrinaPuyaHeiko2024_"})

(defn insert-track [track-metadata]
  (jdbc/insert! db-spec :tracks
                {:timestamp (str (java.time.LocalDateTime/now))
                 :artist track-artist
                 :title track-title
                 :bpm effective-tempo})
  (send-json-to-webapp globals track-metadata))

(when trigger-active?
  (when (not= track-metadata (:last-track @locals))
    (swap! locals assoc :last-track track-metadata)
    (when (some? track-metadata)
      (insert-track track-metadata))))
