import requests
from bs4 import BeautifulSoup

def get_html_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None

url = "https://example.com"
html_content = get_html_data(url)

if html_content is not None:
    soup = BeautifulSoup(html_content, 'html.parser')
    # You can extract specific information or perform other operations here
    print("HTML content:")
    print(soup.prettify())
else:
    print("Failed to fetch data from the URL.")
