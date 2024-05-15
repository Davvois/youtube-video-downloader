import tkinter as tk
from pytube import YouTube

def submitVideoLink():
    videoInput = videoLink.get()
    videoDownload = YouTube(videoInput)
    videoHighestResolution = videoDownload.streams.get_highest_resolution()
    videoHighestResolution.download()

# Inizializzazione della finestra (Tkinter)
window = tk.Tk()
window.geometry("350x200")
window.title("YouTube Video Downloader")
window.resizable(False, False)
window.iconphoto(True, tk.PhotoImage(file="youtube.ico"))

#Titoli e varia roba
title = tk.Label(window, text="Welcome to the YT Video Downloader!", font=('calibre', 15, 'normal'))
title.grid(row=0, column=0)

# Funzionamento principale dell'input e download
videoLink = tk.StringVar()
videoEntry = tk.Entry(window, textvariable=videoLink, font=('calibre', 20, 'normal'))
submitVideoButton = tk.Button(window, text='Submit', command=submitVideoLink, font=('calibre', 20, 'normal'), width=18)
videoEntry.grid(row=1, column=0)
submitVideoButton.grid(row=2, column=0)

if __name__ == "__main__":
    window.mainloop()
