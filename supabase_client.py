import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def is_event_new(link, source):
    table = "scraped_knowafest" if source == "knowafest" else "scraped_unstop"
    result = supabase.table(table).select("id").eq("link", link).execute()
    return len(result.data) == 0

def save_event(name, link, host, desc, participants, source):
    table = "scraped_knowafest" if source == "knowafest" else "scraped_unstop"
    data = {
        "name": name,
        "link": link,
        "hosted_by": host,
        "description": desc,
        "participants": participants,
        "notified": True
    }
    supabase.table(table).insert(data).execute()
