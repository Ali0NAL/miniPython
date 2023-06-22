from pytube import YouTube
import os

url = input("Lütfen bir YouTube linki girin: ")

print("İndiriliyor..")

# DOSYA YOLUNU BELİRT
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/Yotube_video')



# YouTube videonunu indirin ve masaüstüne kaydedin
YouTube(url).streams.first().download(desktop_path)

print("kaydedildi..")