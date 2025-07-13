import requests
from bs4 import BeautifulSoup
from supabase_client import is_event_new, save_event
from telegram_bot import send_telegram_message

BASE_URL = "https://unstop.com/hackathons"

def scrape_unstop():
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text, "html.parser")

    event_cards = soup.find_all("div", class_="styles_card__3cx6D")

    for card in event_cards:
        title = card.find("h2").get_text(strip=True)
        link = "https://unstop.com" + card.find("a")["href"]
        host = card.find("div", class_="styles_eventCard__subInfo__3KeGX").get_text(strip=True)

        # This part may need adjustment if Unstop's HTML changes
        participant_text = card.find("span", string=lambda t: "Participants" in t)
        if participant_text:
            try:
                participants = int(participant_text.get_text(strip=True).split()[0])
            except:
                participants = 0
        else:
            participants = 0

        if "hackathon" in title.lower() and participants >= 5:
            if is_event_new(link, "unstop"):
                message = f"""
🚀 New Hackathon on Unstop!

📛 Name: {title}
🏢 Host: {host}
👥 Participants: {participants}
🔗 Link: {link}
"""
                send_telegram_message(message)
                save_event(title, link, host, None, participants, "unstop")
