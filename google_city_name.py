import requests
from bs4 import BeautifulSoup

cityname = "京都"

url = 'https://www.google.co.jp/search'
#url = 'https://ja.wikipedia.org/wiki/'

req = requests.get(url, params={'q': cityname})

#print(req.url)
#print(req.text)


soup = BeautifulSoup(req.text, 'lxml')

for a in soup.find_all('a'):
      print('https://www.google.co.jp/search'+a.get('href'))

