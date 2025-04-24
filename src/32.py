import requests
from bs4 import BeautifulSoup
import time

def fetch_articles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for article in soup.find_all('div', class_='article'):
        title = article.find('h2').text
        link = article.find('a')['href']
        content = article.find('p').text
        articles.append({
            "title": title,
            "link": link,
            "content": content
        })
    
    return articles

def main():
    url = "https://example.com/articles"  # Replace with the URL of the website you want to scrape
    articles = fetch_articles(url)
    for article in articles:
        print(f"{article['title']}")
        print(article['link'])
        print(article['content'])

if __name__ == "__main__":
    main()
