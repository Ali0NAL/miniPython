import time
import tkinter as tk
from tkinter import messagebox

def zamanlayici(saniye):
    if saniye < 0:
        return None

    for i in range(saniye, -1, -1):
        time.sleep(1)
        dakika, saniye = divmod(i, 60)
        saat, dakika = divmod(dakika, 60)
        saat_label.config(text=f"{saat:02d}:{dakika:02d}:{saniye:02d}")
        root.update()

    messagebox.showinfo("Bitti", "Süre bitti!")

def baslat():
    try:
        saniye = int(saniye_entry.get())
    except ValueError:
        messagebox.showerror("Hata", "Geçersiz giriş! Lütfen bir tam sayı girin.")
        return

    if saniye < 0:
        messagebox.showerror("Hata", "Negatif bir zaman giremezsiniz.")
        return

    zamanlayici(saniye)

root = tk.Tk()
root.title("Dijital Saat Zamanlayıcı")
root.geometry("500x200")  # Ekran boyutunu ayarlar

saniye_label = tk.Label(root, text="Zamanlayıcı için saniye girin:")
saniye_label.pack()

saniye_entry = tk.Entry(root)
saniye_entry.pack()

baslat_button = tk.Button(root, text="Başlat", command=baslat)
baslat_button.pack()

saat_label = tk.Label(root, text="00:00:00", font=("Arial", 50))  # Yazı boyutunu ayarlar
saat_label.pack()

root.mainloop()
