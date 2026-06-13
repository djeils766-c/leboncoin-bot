import requests
import json

TOKEN = "8904724152:AAEMm7xRAoNS4TafgrIzxlW0gdIPgm9XpaE"
CHAT_ID = "8638992678"

SEARCH_URL = "https://www.leboncoin.fr/recherche?category=2&text=polo%205&locations=Sarrebourg_57400__48.73292_7.05234_5000_50000&price=min-7000&mileage=min-160000"

STATE_FILE = "seen.json"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

# Charger annonces déjà vues
try:
    with open(STATE_FILE, "r") as f:
        seen = set(json.load(f))
except:
    seen = set()

def save_state():
    with open(STATE_FILE, "w") as f:
        json.dump(list(seen), f)

def check():
    global seen

    r = requests.get(SEARCH_URL, headers={"User-Agent": "Mozilla/5.0"})
    html = r.text

    # ⚠️ version simple : on récupère des ids d'annonces
    # (Leboncoin change parfois son HTML, mais ça marche souvent)
    parts = html.split('"list_id":"')

    new_found = False

    for p in parts[1:]:
        ad_id = p.split('"')[0]

        if ad_id not in seen:
            seen.add(ad_id)
            new_found = True

            link = f"https://www.leboncoin.fr/ad/voitures/{ad_id}"

            send(f"🚗 Nouvelle annonce détectée !\n\n🔗 {link}")

    if new_found:
        save_state()

check()
