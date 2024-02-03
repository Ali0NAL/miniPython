import tkinter as tk
from tkinter import ttk, filedialog
from pytube import YouTube

def indirme_sureci(stream, chunk, remaining):
    percent = (float(stream.filesize - remaining) / float(stream.filesize)) * float(100)
    indirme_cubugu["value"] = percent
    pencere.update_idletasks()

def dosya_yolu_sec():
    global hedef_dizin
    hedef_dizin = filedialog.askdirectory()
    dosya_yolu_label.config(text=f"Seçilen Dosya Yolu: {hedef_dizin}")

def mp3_indir():
    try:
        youtube_link = link_entry.get()

        # YouTube videosunu indir
        youtube_video = YouTube(youtube_link, on_progress_callback=indirme_sureci)
        video_stream = youtube_video.streams.filter(only_audio=True).first()
        video_stream.download(hedef_dizin)

        durum_label.config(text="Mp3 başarıyla indirildi.", fg="green")
        indirme_cubugu["value"] = 0
    except Exception as e:
        durum_label.config(text=f"Hata: {e}", fg="red")
        indirme_cubugu["value"] = 0

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("YouTube Mp3 İndirici")

# YouTube linki giriş alanı
link_label = tk.Label(pencere, text="YouTube Video Linki:")
link_label.pack(pady=10)
link_entry = tk.Entry(pencere, width=50)
link_entry.pack(pady=10)

# Dosya yolu seçme butonu
dosya_sec_button = tk.Button(pencere, text="Dosya Yolu Seç", command=dosya_yolu_sec)
dosya_sec_button.pack(pady=10)

# Dosya yolu etiketi
dosya_yolu_label = tk.Label(pencere, text="Dosya Yolu:")
dosya_yolu_label.pack(pady=10)

# İndirme butonu
indir_button = tk.Button(pencere, text="Mp3 İndir", command=mp3_indir)
indir_button.pack(pady=10)

# İlerleme çubuğu
indirme_cubugu = ttk.Progressbar(pencere, orient="horizontal", length=300, mode="determinate")
indirme_cubugu.pack(pady=10)

# Durum etiketi
durum_label = tk.Label(pencere, text="")
durum_label.pack(pady=10)

# Başlangıçta dosya yolu belirlemediğimiz için None olarak başlatıyoruz
hedef_dizin = None

# Pencereyi başlat
pencere.mainloop()
