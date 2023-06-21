import requests
import geocoder

def hava_durumu_kontrol():
    # Geocoder kütüphanesiyle konumu otomatik olarak al
    g = geocoder.ip('me')
    enlem = g.lat
    boylam = g.lng
    konum = g.address

    # OpenWeatherMap API'sini kullanarak hava durumu bilgilerini çek
    api_key = "44daba7822f0452efb170202f928d145"  # Replace with your OpenWeatherMap API key
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
        sicaklik_kelvin = hava_durumu["main"]["temp"]
        sicaklik_celsius = sicaklik_kelvin - 273.15
        nem_orani = hava_durumu["main"]["humidity"]


        print("Mevcut konumunuz için hava durumu:")
        print(f"Mevcut konum: {konum}")
        print(f"Sıcaklık: {sicaklik_celsius} °C")
        print(f"Nem Oranı: {nem_orani}%")
    else:
        print("Hava durumu bilgisi alınamadı.")
        print(hava_durumu)

hava_durumu_kontrol()
