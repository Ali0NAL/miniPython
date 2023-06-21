import tkinter as tk
from forex_python.converter import CurrencyRates

def get_exchange_rate(currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(currency, 'TRY')
    result_label.config(text=f"1 {currency} = {exchange_rate} TRY")
    currency_image.config(image=currency_images[currency])

# tkinter uygulamasını oluşturma
root = tk.Tk()
root.title("Döviz Kuru Uygulaması")
root.geometry("500x500")  # Ekran boyutunu ayarlama

# Fotoğrafı yükleme
default_image = tk.PhotoImage(file="C:/Users/app_a/Documents/Python Projects/miniPython/SRC/b.png")
usd_image = tk.PhotoImage(file="C:/Users/app_a/Documents/Python Projects/miniPython/SRC/a.png")
eur_image = tk.PhotoImage(file="C:/Users/app_a/Documents/Python Projects/miniPython/SRC/a.png")

# Ana çerçeve oluşturma
frame = tk.Frame(root)
frame.pack(pady=10)

# Sabit fotoğrafı görüntülemek için etiket oluşturma
currency_image = tk.Label(frame, image=default_image)
currency_image.grid(row=0, column=0, padx=10)

# Döviz kurlarını almak için düğmeleri oluşturma
usd_button = tk.Button(frame, text="USD", command=lambda: get_exchange_rate('USD'))
usd_button.grid(row=1, column=0, pady=5)

eur_button = tk.Button(frame, text="EUR", command=lambda: get_exchange_rate('EUR'))
eur_button.grid(row=2, column=0, pady=5)

# Sonucu görüntülemek için etiket oluşturma
result_label = tk.Label(root, text="", font=("Arial", 13, "bold"))
result_label.pack()

# Döviz kuru fotoğrafı eşleştirmelerini oluşturma
currency_images = {
    'USD': usd_image,
    'EUR': eur_image
}

# Uygulamayı başlatma
root.mainloop()
