import pyaudio
import wave
import os

def convert_to_wav(input_folder, output_folder):
    # İlgili klasördeki tüm dosyaları al
    files = os.listdir(input_folder)

    for file in files:
        # Dosya uzantısını kontrol et (sadece MP4 dosyalarını işle)
        if file.endswith(".mp4"):
            # Dosya yolu oluştur
            input_path = os.path.join(input_folder, file)
            
            # WAV olarak kaydet
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".wav")

            # Ses dosyasını dönüştür
            convert_command = f"ffmpeg -i {input_path} -acodec pcm_s16le -ar 44100 {output_path}"
            os.system(convert_command)

if __name__ == "__main__":
    input_folder = r"C:\Users\app_a\Desktop\Sarkilar"
    output_folder = r"C:\Users\app_a\Desktop\YeniSarkilar"

    convert_to_wav(input_folder, output_folder)
