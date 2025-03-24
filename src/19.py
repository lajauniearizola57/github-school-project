import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch {url} with status code {response.status_code}")
        return None

def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract relevant data from the HTML content
    data = {
        "title": soup.title.text,
        "content": soup.find('div', class_='example-class').text,
        "date": soup.find('time', class_='example-class').get_text(),
        "author": soup.find('span', class_='example-class').text if 'example-class' in str(soup) else None
    }
    
    return data

def main():
    url = 'https://www.example.com'
    html_content = fetch_html(url)
    parsed_data = parse_data(html_content)
    print(parsed_data)

if __name__ == "__main__":
    main()
