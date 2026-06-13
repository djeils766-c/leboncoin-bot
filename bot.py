import requests
import time

TOKEN = "8904724152:AAEMm7xRAoNS4TafgrIzxlW0gdIPgm9XpaE"
CHAT_ID = "8638992678"

URL = "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)

# Exemple simple (tu remplaceras par une vraie URL Leboncoin plus tard)
SEARCH_URL = "https://www.leboncoin.fr/recherche?category=2&text=bmw%20330d"

last_check = ""

def send(msg):
    requests.post(URL, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

def check():
    global last_check

    r = requests.get(SEARCH_URL)
    html = r.text[:2000]

    if html != last_check:
        last_check = html
        send("🚗 Nouvelle annonce détectée sur Leboncoin !")

while True:
    check()
    time.sleep(300)
