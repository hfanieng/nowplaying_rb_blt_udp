import Foundation
import Network

class UDPReceiver: ObservableObject {
    @Published var trackData = TrackData()

    let queue = DispatchQueue(label: "UDP Queue")
    let port: UInt16 = 7000

    init() {
        startReceiving()
    }

    func startReceiving() {
        let params = NWParameters.udp
        let listener = try! NWListener(using: params, on: NWEndpoint.Port(rawValue: port)!)

        listener.newConnectionHandler = { connection in
            connection.start(queue: self.queue)

            connection.receiveMessage { data, context, isComplete, error in
                if let data = data {
                    self.handleReceivedData(data)
                }
            }
        }

        listener.start(queue: self.queue)
    }

    func handleReceivedData(_ data: Data) {
        do {
            if let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any] {
                DispatchQueue.main.async {
                    self.trackData.update(with: json)
                }
            }
        } catch {
            print("Error decoding JSON: \(error)")
        }
    }
}