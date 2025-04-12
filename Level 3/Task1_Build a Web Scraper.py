import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')

        print("\n📰 Extracted Titles:\n")
        for heading in soup.find_all(['h1', 'h2', 'h3']):
            text = heading.get_text(strip=True)
            if text:
                print(f"- {text}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")

# Example usage
url = input("Enter a URL to scrape (e.g., https://news.ycombinator.com): ")
scrape_titles(url)
