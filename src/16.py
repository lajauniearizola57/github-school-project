import requests
from bs4 import BeautifulSoup
import re

def extract_licenses(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    licenses = []
    
    for link in soup.find_all('a'):
        href = link.get('href')
        
        if href.startswith('/licensing/') or href.startswith('/terms-of-service/'):
            text = re.sub(r'https?:\/\/.*', '', href)
            license_info = {
                'file_name': text,
                'url': f'https://www.licenses.google.com/{text}'
            }
            licenses.append(license_info)

    return licenses

licenses_url = "https://www.googleapis.com/drinkslist/v1/products"
licenses = extract_licenses(licenses_url)
for license in licenses:
    print(f"License: {license['file_name']}")
    print(f"URL: {license['url']}")
