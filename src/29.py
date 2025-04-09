import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve data from {url}.")
        return None

def parse_html(html_content, tag_name):
    soup = BeautifulSoup(html_content, "html.parser")
    elements = soup.find_all(tag_name)
    if not elements:
        print("No elements found in the HTML content.")
        return []
    
    parsed_data = [{'text': element.text} for element in elements]
    return parsed_data

url = "https://www.example.com"
html_content = fetch_html(url)
parsed_data = parse_html(html_content, "p")

if parsed_data:
    for data in parsed_data:
        print(data['text'])
else:
    print("Failed to parse the HTML content.")
