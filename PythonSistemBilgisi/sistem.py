import platform
import psutil
import tkinter as tk

def get_system_info():
    # İşletim sistemi bilgilerini al
    os_name = platform.system()
    os_version = platform.version()

    # İşlemci bilgilerini al
    cpu_info = platform.processor()

    # Bellek bilgilerini al
    mem_info = psutil.virtual_memory()
    total_memory = mem_info.total // (1024**3)  # GB cinsinden toplam bellek

    # Disk bilgilerini al
    disk_info = psutil.disk_usage('/')
    total_disk = disk_info.total // (1024**3)  # GB cinsinden toplam disk alanı
    used_disk = disk_info.used // (1024**3)  # GB cinsinden kullanılan disk alanı
    free_disk = disk_info.free // (1024**3)  # GB cinsinden boş disk alanı

    # Ağ bilgilerini al
    net_info = psutil.net_if_addrs()
    ip_addresses = []
    for interface, addresses in net_info.items():
        for address in addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                ip_addresses.append(address.address)

    # Bilgiyi bir metin olarak oluştur
    info_text = f"İşletim Sistemi: {os_name} {os_version}\n" \
                f"İşlemci: {cpu_info}\n" \
                f"Bellek: {total_memory} GB\n" \
                f"Disk: Toplam: {total_disk} GB, Kullanılan: {used_disk} GB, Boş: {free_disk} GB\n" \
                "IP Adresleri:\n" + '\n'.join(ip_addresses)

    return info_text

def show_system_info():
    system_info = get_system_info()
    info_window = tk.Toplevel()
    info_window.title("Sistem Bilgileri")
    info_window.geometry("400x300")
    info_label = tk.Label(info_window, text=system_info, justify="left", padx=10, pady=10)
    info_label.pack()

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Sistem Bilgileri")
root.geometry("200x100")

# Sistem bilgilerini göstermek için bir düğme ekle
info_button = tk.Button(root, text="Sistem Bilgilerini Göster", command=show_system_info)
info_button.pack(pady=20)

# Uygulamayı çalıştır
root.mainloop()
