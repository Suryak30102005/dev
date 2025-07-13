import requests
from bs4 import BeautifulSoup
from supabase_client import is_event_new, save_event
from telegram_bot import send_telegram_message

BASE_URL = "https://www.knowafest.com/explore/technical-fests"

def scrape_knowafest():
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text, "html.parser")

    events = soup.find_all("div", class_="eventlist")

    for event in events:
        title = event.find("a").get_text(strip=True)
        link = "https://www.knowafest.com" + event.find("a")["href"]
        desc = event.find("p").get_text(strip=True)
        host = event.find("h4").get_text(strip=True)

        if "hackathon" in title.lower() or "hackathon" in desc.lower():
            if is_event_new(link, "knowafest"):
                message = f"""
🚀 New Hackathon Found (KnowAFest)!

📛 Name: {title}
🏢 Host: {host}
🔗 Link: {link}
📝 Description: {desc[:150]}...
"""
                send_telegram_message(message)
                save_event(title, link, host, desc, None, "knowafest")
