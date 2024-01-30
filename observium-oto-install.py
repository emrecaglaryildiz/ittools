import paramiko

# Değişkenleri güncelleyin
ssh_username = "user"
ssh_password = "password"
sudo_password = "password"  # SSH şifresiyle aynı olduğunu varsaydık
observium_script_path = "/srv/observium.sh"
ip_list_file = "liste.txt"  # Sunucu IP'lerini içeren dosyanın adı

def run_ssh_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdout.read().decode()

def main():
    try:
        # Sunucu IP'lerini dosyadan okuma
        with open(ip_list_file, "r") as file:
            server_ips = [line.strip() for line in file.readlines()]

        for ip in server_ips:
            try:
                # SSH bağlantısı kurma
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, username=ssh_username, password=ssh_password)

                # sudo -s komutunu girme
                sudo_command = "sudo -S -s"
                ssh.sendline(sudo_command)
                ssh.sendline(sudo_password)
                ssh.recv(1000)  # Gelen çıktıyı atla

                # .sh dosyasını kopyalama ve çalıştırma
                scp = ssh.open_sftp()
                scp.put("local_path_to_script.sh", observium_script_path)
                run_ssh_command(ssh, f"chmod +x {observium_script_path}")
                run_ssh_command(ssh, observium_script_path)

                # Bağlantıyı kapatma
                ssh.close()
                print(f"Observium kurulumu tamamlandı: {ip}")
            except Exception as e:
                print(f"Hata oluştu: {ip} - {str(e)}")
    except FileNotFoundError:
        print(f"{ip_list_file} dosyası bulunamadı.")

if __name__ == "__main__":
    main()
