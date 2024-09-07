import time
from ping3 import ping
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# IP adreslerini dosyadan oku
def load_ip_list(file_path):
  with open(file_path, 'r') as file:
      return [line.strip() for line in file.readlines()]

# E-posta ayarları
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_user = "your_email@example.com"
smtp_password = "your_password"
to_email = "deneme@mail.com"

# Ping kontrol fonksiyonu
def check_servers(ip_list):
  failed_attempts = {ip: 0 for ip in ip_list}
  
  while True:
      for ip in ip_list:
          response = ping(ip)
          if response is None:
              failed_attempts[ip] += 1
              if failed_attempts[ip] >= 3:
                  send_email(ip)
          else:
              failed_attempts[ip] = 0
      time.sleep(30)

# E-posta gönderme fonksiyonu
def send_email(ip):
  msg = MIMEMultipart()
  msg['From'] = smtp_user
  msg['To'] = to_email
  msg['Subject'] = f"Ping Uyarısı: {ip} erişilemiyor"
  
  body = f"{ip} adresine 3 kez üst üste ping atılamadı."
  msg.attach(MIMEText(body, 'plain'))
  
  try:
      server = smtplib.SMTP(smtp_server, smtp_port)
      server.starttls()
      server.login(smtp_user, smtp_password)
      text = msg.as_string()
      server.sendmail(smtp_user, to_email, text)
      server.quit()
      print(f"E-posta gönderildi: {ip}")
  except Exception as e:
      print(f"E-posta gönderilemedi: {e}")

# IP adreslerini yükle ve sunucuları kontrol etmeye başla
ip_list = load_ip_list('ip.txt')
check_servers(ip_list)
