def faktoriyel(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n-1)

try:
    sayi = int(input("Bir sayı girin: "))
except ValueError:
    print("Geçersiz giriş! Lütfen bir tam sayı girin.")
    exit()

if sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
    exit()

sonuc = faktoriyel(sayi)
if sonuc is None:
    print("Geçersiz giriş! Lütfen pozitif bir tam sayı girin.")
else:
    print(sayi, "sayısının faktöriyeli:", sonuc)
