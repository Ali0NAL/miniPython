import cv2
import pytesseract

# Dosya yolu
image_path = "C:/Users/app_a/Documents/Python Projects/miniPython/SRC/k.jpg"

# Fotoğrafı oku
image = cv2.imread(image_path)

# ROI bölgesini belirle
x, y, w, h = 100, 200, 300, 100
roi_image = image[y:y+h, x:x+w]

# ROI'den metni çıkar
roi_text = pytesseract.image_to_string(roi_image, config='--psm 6')

print('Kilometre: ', roi_text)

# Sonuçları kaydet
with open('kilometre.txt', 'w') as file:
    file.write('Kilometre: ' + roi_text)
