import os
import time
from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener, Key  # Key'ı içe aktar
import pyautogui

# Ekran genişliği ve yüksekliği
screen_width, screen_height = pyautogui.size()

# Hedef boyut
target_width, target_height = 740, 1080

# Hedef dosya yolu
save_path = os.path.join("miniPython", "SRC", "screen")

# Kayıt dizinini oluştur
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Ekran görüntüsü al ve belirlediğiniz yere kaydet
def take_screenshot_and_save(index):
    screenshot = pyautogui.screenshot(region=((screen_width - target_width) // 2,
                                           (screen_height - target_height) // 2,
                                           target_width ,
                                           target_height ))

    screenshot_path = os.path.join(save_path, f"screenshot_{index}.png")
    screenshot.save(screenshot_path)

# Fare tıklama olayını dinleme
click_count = 0

def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1
        take_screenshot_and_save(click_count)
        time.sleep(1)  # Her tıklamadan sonra bir saniye beklemek

# Fare tıklama dinleyiciyi başlat
with Listener(on_click=on_click) as listener:
    # Klavye dinleyiciyi başlat
    def on_key_release(key):
        if key == Key.esc:
            listener.stop()
            return False

    with KeyboardListener(on_key_release=on_key_release) as keyboard_listener:
        keyboard_listener.join()
