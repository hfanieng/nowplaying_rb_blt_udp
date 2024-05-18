import socket
import threading
import json
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# URL des Bildes

img_url = "http://127.0.0.1:17081/artwork/1?icons=true"
wave_url = "http://127.0.0.1:17081/wave-detail/1?width=800&scale=2"

#img_url = "http://192.168.178.45:17081/artwork/1?icons=true"
#wave_url = "http://192.168.178.43:17081/wave-detail/1?width=800&scale=2"
#wave_url = "http://192.168.178.45:17081/wave-preview/1?width=1000&height=200"

# defining the Tkinter-window
# Erstellen des Tkinter-Fenster
window = tk.Tk()
#setting the window title
#Festelegen des Fenstertitels
window.title("Now Playing on XDJ-XZ")
#setting the background of the window to black an open it maimized - with title, close and maximize functions enabled
#Festlegen der Hintergrundfarbe des einzigen (Hauptfenster) auf schwarz und maximiertes öffnen
window.configure(bg='black') 
window.state('zoomed') 
# Create labels for song title, cover, artist and other information - which BLT receives from Pro DJ Link:
# Erstellen der Labels für Songtitel, Cover, Interpret und weitere Informationen - welche BLT aus Pro DJ Link empfängt:

# column 0-3 width 240 rowspan 4

cover_label = tk.Label(window, text="Cover", bg='#191919', anchor='n', width=240, height=240) #Zeile 0 (0)
beat1_label = tk.Label(window, text="1", bg="#191919", fg='silver', font=("Arial", 18,), width=60, height=40, padx=10)
# column 1 width 60
beat2_label = tk.Label(window, text="2", bg="#191919", fg='silver', font=("Arial", 18,), width=60, height=40, padx=10)
# column 2 width 60
beat3_label = tk.Label(window, text="3", bg="#191919", fg='silver', font=("Arial", 18,), width=60, height=40, padx=10)
# column 3 width 60
beat4_label = tk.Label(window, text="4", bg="#191919", fg='silver', font=("Arial", 18,), width=60, height=40, padx=10)
# column 4 width 280
title_label = tk.Label (window, text="Titel / Title", bg='#191919', fg='white', font=("Arial", 20), anchor="w", width=280, height=40, padx=10) 
label_label = tk.Label(window, text="", bg='#191919', fg='silver', font=("Arial", 18), anchor='w', width=280, height=40, padx=10) 
genre_label = tk.Label(window, text="Genre", bg='#191919', fg='silver', font=("Arial", 18), anchor='w', width=280, height=40, padx=10)
comment_label = tk.Label(window, text="Kommentar / comment", bg="#191919", fg='silver', font=("Arial", 18,), anchor='w', width=280, height=40, padx=10)
# column 5 with 280
artist_label = tk.Label(window, text="Interpret / Artist", bg='#191919', fg='silver', font=("Arial", 18), anchor='w', width=280, height=40, padx=10)
# column 6 width 160
time_label = tk.Label(window, text="Zeit / Time", bg='#191919', fg='silver', font=("Arial", 18), anchor='w', width=160, height=40, padx=10)
mood_label = tk.Label(window, text="Mood", bg='#191919', fg='black', font=("Arial", 18), anchor='w', width=160, height=40, padx=10)
bank_label = tk.Label(window, text="Bank", bg='#191919', fg='white', font=("Arial", 18), anchor='w', width=160, height=40, padx=10)
phrase_label = tk.Label(window, text="Phrase", bg='#191919', fg='black', font=("Arial", 18), anchor='w', width=160, height=40, padx=10)
# column 7 width 160
key_label = tk.Label(window, text="Key", bg='#191919', fg='silver', font=("Arial", 18), anchor='w', width=160, height=40, padx=10)
beat_label = tk.Label(window, text="Beat", bg='#191919', fg='silver', font=("Arial", 18), anchor='w', width=160, height=40,padx=10)
section_label = tk.Label(window, text="Section", bg='black', fg='black', font=("Arial", 18), anchor='w', width=160, height=40, padx=10)
# column 8 width 160
bpm_label = tk.Label(window, text="BPM", bg='#191919', fg='silver', font=("Arial", 18), anchor='w', width=160, height=40, padx=10)
# waveform
waveform_label = tk.Label(window, text="Waveform", bg='black', anchor='w', width=1024, height=200, border=0, relief="raised")
#Positioning the label fields and the cover
#Positionieren der Bezeichnungsfelder und des Covers
window.grid_columnconfigure(0, weight=1, minsize=60)
window.grid_columnconfigure(1, weight=1, minsize=60)
window.grid_columnconfigure(2, weight=1, minsize=60)
window.grid_columnconfigure(3, weight=1, minsize=60)
window.grid_columnconfigure(4, weight=1, minsize=280)
window.grid_columnconfigure(5, weight=1, minsize=280)
window.grid_columnconfigure(6, weight=1, minsize=160)
window.grid_columnconfigure(7, weight=1, minsize=160)
window.grid_columnconfigure(8, weight=1, minsize=160)
window.grid_rowconfigure(0, weight=1, minsize=60)
window.grid_rowconfigure(1, weight=1, minsize=60)
window.grid_rowconfigure(2, weight=1, minsize=60)
window.grid_rowconfigure(3, weight=1, minsize=60)
window.grid_rowconfigure(4, weight=1, minsize=80)
window.grid_rowconfigure(5, weight=1, minsize=320)
window.grid_rowconfigure(6, weight=1, minsize=320)
# row 0
cover_label.grid(row=0, column=0, rowspan=4, columnspan=4)
title_label.grid(row=0, column=4, padx=2, pady=2)
artist_label.grid(row=0, column=5, padx=2, pady=2)
key_label.grid(row=0, column=6, padx=2, pady=2)
time_label.grid(row=0, column=7, padx=2, pady=2)
bpm_label.grid (row=0, column=8, padx=2, pady=2)
# row 1
label_label.grid(row=1, column=4, padx=2, pady=2)
mood_label.grid(row=1, column=6, padx=2, pady=2)
beat_label.grid(row=1, column=8, padx=2, pady=2)
# row 2
genre_label.grid(row=2, column=4, padx=2, pady=2)
bank_label.grid(row=2, column=6, padx=2, pady=2)
# row 3
comment_label.grid(row=3, column=4, padx=2, pady=2)
phrase_label.grid(row=3, column=6,  padx=2, pady=2)
section_label.grid(row=3, column=7, padx=2, pady=2)
# row 4
beat1_label.grid(row=4, column=0, padx=2, pady=2)
beat2_label.grid(row=4, column=1, padx=2, pady=2)
beat3_label.grid(row=4, column=2, padx=2, pady=2)
beat4_label.grid(row=4, column=3, padx=2, pady=2)
# row 5
waveform_label.grid(row=5, column=0, columnspan=8)

def socket_receiver():
    # creating a UDP socket
    # Erstellen eines UDP-Sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 7000
    sock.bind(('', port))
    #print("Socket verbunden mit Port", port)
    receiving = True
    while receiving:
        print('\nWarten auf eine Nachricht')
        data, address = sock.recvfrom(4096)
        print('Erhaltene {} Bytes von {}'.format(len(data), address))
        print(data)
        json_data = json.loads(data)
        # artist
        artist_label.config (text=json_data['trackArtist'])
        # artwork
        response = requests.get(img_url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)), size=(240, 240))
        cover_label.configure(image=img)
        cover_label.image = img
        # bank
        bank_label.config(text=json_data['trackBank'])
        # beat
        beat = json_data['beat']
        beat_label.config(text=beat)
        print (beat)
        if beat == 1:
            beat1_label.config(bg='green')
            print ("Beat 1")
        else: beat1_label.config(bg='#191919')
        if beat == 2:
            beat2_label.config(bg='green')
            print ("Beat 2")
        else: beat2_label.config(bg='#191919')
        if beat == 3:
            beat3_label.config(bg='green')
        else: beat3_label.config(bg='#191919')
        if beat == 4:
            beat4_label.config(bg='green')
        else: beat4_label.config(bg='#191919')
            
        # bpm
        bpm_label.config(text=json_data['bpm'])
        # cooment
        comment_label.config(text=json_data['trackComment'])
        # genre
        genre_label.config(text=json_data['trackGenre'])
        # key
        key_label.config(text=json_data['trackKey'])
        # label
        label_label.config(text=json_data['trackLabel'])
        # phrase / mood
        phrase_label.config(text=json_data['phraseType'])
        phrase = json_data['phraseType']
        if "intro" in phrase:
            phrase_label.config(bg='#DA4F4D', text="Intro")
        elif "intro-1" in phrase:
            phrase_label.config(bg='#000000', text="Intro 1")
        elif "intro-2" in phrase:
            phrase_label.config(bg='#C43800', text="Intro 2")
        elif "verse-1" in phrase:
            phrase_label.config(bg='#6A76FF', text="Verse 1")
        elif "verse-2" in phrase:
            phrase_label.config(bg='#685AFF', text="Verse 2")
        elif "verse-3" in phrase:
            phrase_label.config(bg='#7854FF', text="Verse 3")
        elif "verse-4" in phrase:
            phrase_label.config(bg='#8854FF', text="Verse 4")
        elif "verse-5" in phrase:
            phrase_label.config(bg='#9954FF', text="Verse 5")
        elif "verse-6" in phrase:
            phrase_label.config(bg='#AA54FF', text="Verse 6")
        elif "bridge" in phrase:
            phrase_label.config(bg='#E1DD28', text="Bridge")
        elif "up-1" in phrase:
            phrase_label.config(bg='#972CFF', text="Up 1")
        elif "up-2" in phrase:
            phrase_label.config(bg='#7A2DFF', text="Up 2")
        elif "up-3" in phrase:
            phrase_label.config(bg='#6E2DFF', text="Up 3")
        elif "chorus" in phrase:
            phrase_label.config(bg='#8BCB82', text="Chorus")
        elif "chorus-1" in phrase:
            phrase_label.config(bg='#38B500', text="Chorus 1")
        elif "down" in phrase:
            phrase_label.config(bg='#A07F26', text="Down")
        elif "outro" in phrase:
            phrase_label.config(bg='#818DA1', text="Outro")
        elif "outro-1" in phrase:
            phrase_label.config(bg='#6791CE', text="Outro 1")
        elif "outro-2" in phrase:
            phrase_label.config(bg='#7291BA', text="Outro 2")
        mood = phrase.split("-") [0]
        if "low" in phrase:
            mood_label.config(bg='#4FC0F8',text="Low")
        elif "mid" in phrase:
            mood_label.config(bg='#F8E331',text="Mid")
        elif "high" in phrase:
            mood_label.config(bg='#46E000',text="High")
        # section
        section = json_data['phraseSection']
        section_label.config(text=section)
        if "start" in section:
            section_label.config(bg='#A5FF8F', text="Start")
        elif "loop" in section:
            section_label.config(bg='#9F97FF', text="Loop")
        elif "end" in section:
            section_label.config(bg='#FFA5A5', text="End")
        elif "fill" in section:
            section_label.config(bg='#D27CFF', text="Fill")
        # time reached
        seconds, milliseconds = divmod(json_data['trackTimereached'], 1000)
        minutes, seconds = divmod(seconds, 60)
        time = (f"{minutes:02}:{seconds:02}")
        time_label.config(text=time)
        # title
        title_label.config (text=json_data['trackTitle'])
        # waveform        
        response = requests.get(wave_url)
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)), size=(500, 100))
        waveform_label.configure(image=img)
        waveform_label.image = img
        
        if "\n" in json_data:
            print("Ende der Nachricht")
            receiving = False

# Erstellen Sie einen Thread, der die socket_receiver-Funktion ausführt
t = threading.Thread(target=socket_receiver)

# Starten Sie den Thread
# stream.start()
t.start()

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)
# Starten Sie das Fenster
# Start the window
window.mainloop()
