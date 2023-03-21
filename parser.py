import requests
from bs4 import BeautifulSoup


url = 'https://poliglot16.ru/slova-po-teme/angliyskie-prilagatelnye/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
tbody = soup.find('tbody').find_all('tr', class_='text-left')


for i in tbody:
    print(i.find('b', class_='text-black').text)
    eng_rus = i.find_all('div', class_='small')
    print(eng_rus[0].text)
    print(eng_rus[1].text)
    print(i.find('td', class_='small text-muted').text)
    print()



