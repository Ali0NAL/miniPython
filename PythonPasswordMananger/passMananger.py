import random
import string
import tkinter as tk
from tkinter import messagebox

# Şifre oluşturma fonksiyonu
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Yeni şifre oluşturma işlevi
def create_password():
    site_name = site_entry.get()
    password_length = int(length_entry.get())
    password = generate_password(password_length)
    passwords[site_name] = password
    messagebox.showinfo("Yeni Şifre", f"{site_name} için oluşturulan şifre:\n{password}")
    site_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    save_passwords()

# Şifreyi kopyalama işlevi
def copy_password():
    selected_index = password_list.curselection()
    if selected_index:
        selected_password = password_list.get(selected_index)
        password = selected_password.split(" - Şifre: ")[1]  # Şifre bölümünü ayırma
        password_text.delete(0, tk.END)
        password_text.insert(tk.END, password)
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Kopyalandı", "Şifre panoya kopyalandı.")

# Şifreleri listeleme işlevi
def list_passwords():
    password_list.delete(0, tk.END)
    for site, password in passwords.items():
        password_list.insert(tk.END, f"Site/Adres: {site} - Şifre: {password}")

# Şifreleri dosyaya kaydetme işlevi
def save_passwords():
    with open("passwords.txt", "w") as file:
        for site, password in passwords.items():
            file.write(f"{site}:{password}\n")

# Şifreleri dosyadan yükleme işlevi
def load_passwords():
    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    site, password = line.split(":")
                    passwords[site] = password
    except FileNotFoundError:
        pass

# Anahtar-Değer çiftlerini tutacak bir sözlük
passwords = {}

# Şifreleri dosyadan yükle
load_passwords()

# Tkinter uygulamasını oluşturma
root = tk.Tk()
root.title("Şifre Yöneticisi")
root.geometry("500x400")  # Ekran boyutunu ayarlama


# Site ve şifre uzunluğu giriş alanları
site_label = tk.Label(root, width=100, font=13, text="SİTE:")
site_label.pack()
site_entry = tk.Entry(root)
site_entry.pack()

length_label = tk.Label(root, font=13, text="Şifre karakter uzunluğu:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Yeni şifre oluşturma düğmesi
create_button = tk.Button(root,font=13, text="Yeni Şifre Oluştur", command=create_password)
create_button.pack()

# Şifreleri listeleme düğmesi
list_button = tk.Button(root, font=13, text="Şifreleri Listele", command=list_passwords)
list_button.pack()

# Şifre listesi
password_frame = tk.Frame(root)
password_frame.pack()

password_scrollbar = tk.Scrollbar(password_frame)
password_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

password_list = tk.Listbox(password_frame, width=70, height=10, yscrollcommand=password_scrollbar.set)
password_list.pack(side=tk.LEFT, fill=tk.BOTH)

password_scrollbar.config(command=password_list.yview)

# Şifre kopyalama düğmesi
copy_button = tk.Button(root, font=13,  text="Şifreyi Kopyala", command=copy_password)
copy_button.pack()

# Şifre metin alanı
password_text = tk.Entry(root, width=60)
password_text.pack()

# Uygulamayı başlatma
root.mainloop()
