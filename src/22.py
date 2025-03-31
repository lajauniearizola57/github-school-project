import requests
from bs4 import BeautifulSoup
import re

def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
    except Exception as e:
        print(f"An error occurred: {e}")

url = "https://example.com"
soup = scrape_website(url)

if soup:
    title = soup.find('h1', class_='post-title').text.strip()
    author = soup.find('span', class_='post-author').text.strip()

    content = soup.get_text(strip=True)
    
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(content)
else:
    print("Failed to retrieve the website.")
