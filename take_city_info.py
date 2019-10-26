import requests

cityname = "京都"

url = 'https://www.google.co.jp/search'

req = requests.get(url, params={'q': cityname})

req.url

print(req.text)
