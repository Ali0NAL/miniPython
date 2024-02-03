from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup

def arabam_crawler_selenium():
    # Selenium WebDriver'ı başlat
    service = ChromeService('C:/WebDriver/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # Arabam.com üzerindeki ikinci el otomobil sayfası
    url = "https://www.arabam.com/ikinci-el/otomobil"
    
    # Web sayfasını aç
    driver.get(url)

    # Sayfanın tamamen yüklenmesini bekle
    driver.implicitly_wait(10)

    # Sayfanın kaynak kodunu al
    html_content = driver.page_source

    # BeautifulSoup ile HTML'i parse et
    soup = BeautifulSoup(html_content, 'html.parser')

    # Tüm ilanları içeren tr'yi bul
    ilan_tr_list = soup.find_all('tr', class_='listing-list-item')

    # Her bir ilanın içinde dolaşarak bilgileri çek
    for ilan_tr in ilan_tr_list:
        marka_model_element = ilan_tr.find('div', class_='listing-text-new')
        fiyat_element = ilan_tr.find('span', class_='listing-price')
        yil_element = ilan_tr.find('div', class_='fade-out-content-wrapper').find('a')

        # None kontrolü ekle ve ardından metin özelliğine eriş
        marka_model = marka_model_element.text.strip() if marka_model_element else "Bilgi Bulunamadı"
        fiyat = fiyat_element.text.strip() if fiyat_element else "Bilgi Bulunamadı"
        yil = yil_element.text.strip() if yil_element else "Bilgi Bulunamadı"

        # Bilgileri yazdır
        print("Marka ve Model:", marka_model)
        print("Fiyat:", fiyat)
        print("Yıl:", yil)
        print("-" * 30)

    # WebDriver'ı kapat
    driver.quit()

if __name__ == "__main__":
    arabam_crawler_selenium()
