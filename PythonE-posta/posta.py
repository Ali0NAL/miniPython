import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # E-posta sunucusu ayarları
    smtp_server = 'smtp.gmail.com'  # Gmail için örnek. Diğer e-posta sağlayıcıları için ayarlar farklı olabilir.
    smtp_port = 587  # TLS bağlantısı için kullanılan port numarası

    try:
        # E-posta mesajını oluşturma
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject

        # E-posta gövdesini ekleyin
        message.attach(MIMEText(body, 'plain'))

        # E-posta gönderme işlemi
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # TLS güvenli bağlantı başlat
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            

        print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"E-posta gönderme hatası: {e}")

# Kullanıcı bilgilerini girin
sender_email = "alıcı e-posta adresiniz"
sender_password = "şifreniz"
receiver_email = "tahaegeaydin19@gmail.com"
subject = "başlık"
body = "Bu bir test e-postasıdır."


# E-posta gönderme işlemi
send_email(sender_email, sender_password, receiver_email, subject, body)

