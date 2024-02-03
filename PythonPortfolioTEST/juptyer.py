import pandas as pd
import numpy as np

# Excel dosyasından veriyi yükle
dosyadi = r'C:\Users\app_a\Documents\Python Projects\miniPython\SRC\veri.xlsx'
veri = pd.read_excel(dosyadi, sheet_name=None, header=0, usecols="A:X")

print(veri)
