import http.client
import json
import pandas as pd
import os

# API host ve endpoint bilgileri
api_host = "api.collectapi.com"
api_path = "/economy/hisseSenedi"

# API anahtarınızı burada saklayın
api_key = "apikey 0fRScGBxA0koJuF8NR8Txt:2FvF0AgQ9B2mJFyyoERthg"

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'apikey {api_key}'
}

# HTTPS bağlantısı oluşturun
conn = http.client.HTTPSConnection(api_host)

# Başlık bilgileri ile GET isteği yapın
conn.request("GET", api_path, headers=headers)

res = conn.getresponse()
data = res.read()

# JSON veriyi bir Python sözlüğüne çevirin
data_dict = json.loads(data)

# JSON veriyi bir Pandas DataFrame'e dönüştürün
df = pd.DataFrame(data_dict["result"])

# Masaüstü yolunu alın
desktop_path = os.path.expanduser("~/Desktop")  # Kullanıcının masaüstü yolunu alır

# Excel dosyasını oluşturun ve verileri yazdırın
excel_file_path = os.path.join(desktop_path, "hisse_senedi_verileri.xlsx")

df.to_excel(excel_file_path, sheet_name="Hisse Senedi Verileri", index=False)

print(f"Excel dosyası {excel_file_path} olarak kaydedildi.")
