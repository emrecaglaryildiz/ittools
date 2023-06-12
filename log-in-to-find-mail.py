import re
import csv

# Log dosyasının yolu
log_file = "/var/log/mail.log"

# Hedef CSV dosyasının yolu
output_file = "/path/to/output.csv"

# E-posta adreslerini içeren bir liste oluşturun
email_addresses = []

# Log dosyasını okuyun
with open(log_file, "r") as file:
    # Her satırı kontrol edin
    for line in file:
        # E-posta adreslerini arayın ve listeye ekleyin
        matches = re.findall(r"to=<([^>]+)>", line)
        email_addresses.extend(matches)

# E-posta adreslerini CSV dosyasına yazın
with open(output_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Email Address"])  # Başlık satırını yazın
    for address in email_addresses:
        writer.writerow([address])

print("E-posta adresleri başarıyla CSV dosyasına yazıldı:", output_file)

