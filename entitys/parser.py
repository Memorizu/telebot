import requests
from bs4 import BeautifulSoup

url = 'https://www.kinopoisk.ru/lists/categories/movies/1/'

status = requests.get(url)

bsoup = BeautifulSoup(status.text)
print(bsoup)