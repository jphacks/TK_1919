import requests
from bs4 import BeautifulSoup
import bs4
from urllib.parse import quote

cityname = "京都"

#url = 'https://www.google.co.jp/search'
#url = 'https://ja.wikipedia.org/wiki/'
#url = 'http://www.yahoo.co.jp'
#url = "https://search.yahoo.co.jp/search?p={}&n=60".format(quote(cityname))
https://www.arukikata.co.jp/city/AMS/

resp = requests.get(url, params={'q': cityname})
print(resp.text)

resp.raise_for_status()

# 取得したHTMLをパースする
soup = bs4.BeautifulSoup(resp.text, "html.parser")

for aa in soup.find_all("a"):
            link = aa.get("href").replace('/url?q=','')
            name = aa.get_text()
            print(link,"\t",name)
