import requests
from bs4 import BeautifulSoup
import bs4
from urllib.parse import quote

def yahooScrapingCity(cityname) :

    #url = 'https://www.google.co.jp/search'
    #url = 'https://ja.wikipedia.org/wiki/'
    #url = 'http://www.yahoo.co.jp'
    url = "https://search.yahoo.co.jp/search?p={}&n=60".format(quote(cityname))
    #url = "https://www.arukikata.co.jp/city/AMS/"

    resp = requests.get(url, params={'q': cityname})
    #print(resp.text)

    resp.raise_for_status()

    # 取得したHTMLをパースする
    soup = bs4.BeautifulSoup(resp.text, "html.parser")

    #data = [[0]*5 for i in range(5)];
    data = []

    #print(soup.find_all("a"))

    for aa in soup.find_all("a")[3:8]:
                link = aa.get("href").replace('/url?q=','')
                name = aa.get_text()
                data1 = []
                data1.append(cityname)
                data1.append(name)
                data1.append(link)
                data.append(data1)
                #print(link,"\t",name)
    return data

path_w = 'cityurldata.txt'

SearchName = ['東京', '京都', '北海道', '沖縄', 'ジャカルタ', 'ハノイ', 'アムステルダム', 'パリ', 'ソウル', 'ホノルル', 'セブ', 'バンコク', 'ロンドン', 'ニューヨーク', 'チューリッヒ', 'テキサス', 'エジプト', '北京', '上海', 'ベルリン']


for i in SearchName :
    data = yahooScrapingCity(i)
    with open(path_w, mode='a') as f:
        f.write(str(data)+'\n')
