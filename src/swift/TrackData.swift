import Foundation

struct TrackData {
    var phraseType = ""
    var trackKey = ""
    var trackComment = ""
    var masterPlayerNumber = 0
    var trackTimeReached = 0
    var phraseSection = ""
    var trackArtist = ""
    var trackGenre = ""
    var bpm: Double = 0.0
    var trackBank = ""
    var fill = false
    var beat = 0
    var trackTitle = ""
    var trackLabel: String? = nil

    mutating func update(with json: [String: Any]) {
        self.phraseType = json["phraseType"] as? String ?? ""
        self.trackKey = json["trackKey"] as? String ?? ""
        self.trackComment = json["trackComment"] as? String ?? ""
        self.masterPlayerNumber = json["masterPlayerNumber"] as? Int ?? 0
        self.trackTimeReached = json["trackTimereached"] as? Int ?? 0
        self.phraseSection = json["phraseSection"] as? String ?? ""
        self.trackArtist = json["trackArtist"] as? String ?? ""
        self.trackGenre = json["trackGenre"] as? String ?? ""
        self.bpm = json["bpm"] as? Double ?? 0.0
        self.trackBank = json["trackBank"] as? String ?? ""
        self.fill = json["fill"] as? Bool ?? false
        self.beat = json["beat"] as? Int ?? 0
        self.trackTitle = json["trackTitle"] as? String ?? ""
        self.trackLabel = json["trackLabel"] as? String
    }
}