import SwiftUI

struct ContentView: View {
    @ObservedObject var udpReceiver = UDPReceiver()

    var body: some View {
        VStack(alignment: .leading) {
            Text("Track Information")
                .font(.largeTitle)
                .padding()

            Text("Track Title: \(udpReceiver.trackData.trackTitle)")
            Text("Artist: \(udpReceiver.trackData.trackArtist)")
            Text("Genre: \(udpReceiver.trackData.trackGenre)")
            Text("Key: \(udpReceiver.trackData.trackKey)")
            Text("BPM: \(udpReceiver.trackData.bpm)")
            Text("Phrase Type: \(udpReceiver.trackData.phraseType)")
            Text("Phrase Section: \(udpReceiver.trackData.phraseSection)")
            Text("Master Player Number: \(udpReceiver.trackData.masterPlayerNumber)")
            Text("Time Reached: \(udpReceiver.trackData.trackTimeReached)")
            Text("Comment: \(udpReceiver.trackData.trackComment)")
            Text("Track Bank: \(udpReceiver.trackData.trackBank)")
            Text("Fill: \(udpReceiver.trackData.fill ? "Yes" : "No")")
            Text("Beat: \(udpReceiver.trackData.beat)")
            Text("Label: \(udpReceiver.trackData.trackLabel ?? "N/A")")
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}