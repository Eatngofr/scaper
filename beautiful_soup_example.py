from bs4 import BeautifulSoup
import requests

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = [p.text for p in soup.find_all('p')]
    return paragraphs

if __name__ == "__main__":
    url = 'https://lionofficiel.blogspot.com'
    data = scrape_website(url)
    print(data)
