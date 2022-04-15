import requests
from bs4 import BeautifulSoup

url = 'https://sofifa.com'

page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(page.content, 'html.parser')


teste = soup.find('tbody', class_='list').find_all('tr')

for i in teste:
    print(f"{i.find('td', class_='col-name').find('a').text} Age: {i.find('td', class_='col col-ae').text} Salário: {i.find('td', class_='col col-wg').text}")