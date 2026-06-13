import requests
import os

TOKEN = "8904724152:AAEMm7xRAoNS4TafgrIzxlW0gdIPgm9XpaE"
CHAT_ID = "8638992678"

URLS = [
    "https://www.leboncoin.fr/recherche?category=2&text=polo%205&locations=Sarrebourg_57400__48.73292_7.05234_5000_50000&price=min-7000&mileage=min-160000",
    "https://www.leboncoin.fr/recherche?category=2&text=polo+tdi&locations=Sarrebourg_57400__48.73292_7.05234_5000_50000&price=min-7000&mileage=min-160000&kst=k"
]

# mémoire simple en RAM (anti doublons)
seen = set()

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check(url):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = r.text

    parts = html.split('"list_id":"')

    for p in parts[1:]:
        ad_id = p.split('"')[0]

        if ad_id not in seen:
            seen.add(ad_id)

            link = f"https://www.leboncoin.fr/ad/voitures/{ad_id}"

            send("🚗 Nouvelle annonce Leboncoin !\n" + link)

def main():
    for url in URLS:
        check(url)

    send("✅ Bot OK (check terminé)")

main()
