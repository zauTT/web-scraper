import requests
from bs4 import BeautifulSoup

search = input("Enter the Author: ")

base_url = "https://quotes.toscrape.com/"
page = 1

def scrape_quotes(search, page=1):
    url = f'{base_url}/page/{page}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        author = quote.find('small', class_='author').text
        if search.lower() in author.lower():
            text = quote.find('span', class_='text').text
            print(f'"{text}" - {author}')

    next_button = soup.find('li', class_='next')

    if next_button:
        scrape_quotes(search, page + 1)

scrape_quotes(search)