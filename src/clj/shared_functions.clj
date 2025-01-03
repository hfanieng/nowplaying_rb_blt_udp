(defn send-json-to-webapp
  "Encodes a map as JSON and sends it to the Astro web app."
  [globals m]
  (let [message (str (cheshire.core/encode m) "\n")  ; Encode as JSON line.
        {:keys [webapp-url]} @globals  ; Find where to send.
        response (clj-http.client/post webapp-url {:body message :content-type :json})]
    (println "Response from web app:" response)))
