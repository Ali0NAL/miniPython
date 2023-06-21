import requests
import geocoder

def hava_durumu_kontrol():
    # Geocoder kütüphanesiyle konumu otomatik olarak al
    g = geocoder.ip('me')
    enlem = g.lat
    boylam = g.lng

    # OpenWeatherMap API'sini kullanarak hava durumu bilgilerini çek
    api_key = "44daba7822f0452efb170202f928d145"  # OpenWeatherMap API anahtarını buraya girin
    #Kendi api anahtarınızı kullanıcaksanız 1-2 saat beklemeniz gerekebilir.
    api_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": enlem,
        "lon": boylam,
        "appid": api_key
    }

    response = requests.get(api_url, params=params)
    hava_durumu = response.json()

    if "weather" in hava_durumu:
        # Hava durumu bilgilerini işle ve yazdır
        durum = hava_durumu["weather"][0]["description"]
        sicaklik = hava_durumu["main"]["temp"]
        nem_orani = hava_durumu["main"]["humidity"]

        print("Mevcut konumunuz için hava durumu:")
        print(f"Durum: {durum}")
        print(f"Sıcaklık: {sicaklik} Kelvin")
        print(f"Nem Oranı: {nem_orani}%")
    else:
        print("Hava durumu bilgisi alınamadı.")
        print(hava_durumu)

hava_durumu_kontrol()
