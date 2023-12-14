import requests
import csv

# Aseta oma groupid
groupid = "oma_groupid"

# HTTP-rajapinnan osoite
url = f"http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=17"

# Tee HTTP-pyyntö ja hae data
response = requests.get(url)

# Tarkista, että pyyntö onnistui
if response.status_code == 200:
    # Muunnetaan vastaus tekstiksi
    data = response.text

    # Erota data riveihin ja sarakkeisiin
    lines = data.splitlines()
    data = [line.split(',') for line in lines]

    # Tallenna data CSV-tiedostoksi
    with open('datakannasta.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Data tallennettu tiedostoon 'datakannasta.csv'")
else:
    print("Virhe datan haussa:", response.status_code)
