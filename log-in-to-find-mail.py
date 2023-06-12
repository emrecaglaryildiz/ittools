import re

# Log dosyasının yolu
log_file = "/var/log/mail.log"

# Hedef dosyanın yolu
output_file = "/path/to/output.txt"

# E-posta adreslerini içeren bir liste oluşturun
email_addresses = []

# Log dosyasını okuyun
with open(log_file, "r") as file:
    # Her satırı kontrol edin
    for line in file:
        # E-posta adreslerini arayın ve listeye ekleyin
        matches = re.findall(r"to=<([^>]+)>", line)
        email_addresses.extend(matches)

# E-posta adreslerini hedef dosyaya yazın
with open(output_file, "w") as file:
    for address in email_addresses:
        file.write(address + "\n")

print("E-posta adresleri başarıyla çıktı dosyasına yazıldı: ", output_file)
