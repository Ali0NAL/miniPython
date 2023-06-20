def asal_mi(sayi):
    if sayi < 2:
        return False

    if sayi == 2 or sayi == 3:
        return True

    if sayi % 2 == 0 or sayi % 3 == 0:
        return False

    i = 5
    while i * i <= sayi:
        if sayi % i == 0 or sayi % (i + 2) == 0:
            return False
        i += 6

    return True

sayi = input("Bir sayı girin: ")

try:
    sayi = int(sayi)
except ValueError:
    print("Geçersiz giriş! Lütfen bir sayı girin.")
    exit()

if sayi < 0:
    print("Negatif sayılar asal değildir.")
    exit()

if asal_mi(sayi):
    print(sayi, "bir asal sayıdır.")
else:
    print(sayi, "bir asal sayı değildir.")
