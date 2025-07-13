from scraper_knowafest import scrape_knowafest
from scraper_unstop import scrape_unstop

def main():
    print("🔍 Starting hackathon scraping and notification...")
    scrape_knowafest()
    scrape_unstop()
    print("✅ Done!")

if __name__ == '__main__':
    main()
