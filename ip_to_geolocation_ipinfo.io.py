import requests

api_token = "3b034739f19d17"

def get_country(ip):
    url = f"https://ipinfo.io/{ip}/country?token={api_token}"
    response = requests.get(url)
    return response.text.strip()

def get_city(ip):
    url = f"https://ipinfo.io/{ip}/city?token={api_token}"
    response = requests.get(url)
    return response.text.strip()

def get_region(ip):
    url = f"https://ipinfo.io/{ip}/region?token={api_token}"
    response = requests.get(url)
    return response.text.strip()

def get_timezone(ip):
    url = f"https://ipinfo.io/{ip}/timezone?token={api_token}"
    response = requests.get(url)
    return response.text.strip()

def main():
    ip_list = []
    with open("ip_list.txt", "r") as file:
        ip_list = [line.strip() for line in file.readlines()]

    print("| IP Address    | Country Code | City         | Region       | Timezone     |")
    print("+---------------+--------------+--------------+--------------+--------------+")

    for ip in ip_list:
        country = get_country(ip)
        city = get_city(ip)
        region = get_region(ip)
        timezone = get_timezone(ip)
        print(f"| {ip:<13} | {country:<12} | {city:<12} | {region:<12} | {timezone:<12} |")

if __name__ == "__main__":
    main()
