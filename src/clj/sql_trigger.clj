(ns your-namespace)
  (add-library '[org.clojure/java.jdbc "0.7.12"])
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
                 :bpm effective-tempo}))

(when trigger-active?
  (when (not= track-metadata (:last-track @locals))
    (swap! locals assoc :last-track track-metadata)
    (when (some? track-metadata)
      (insert-track track-metadata))))
