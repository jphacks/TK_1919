import requests
from bs4 import BeautifulSoup
import bs4
from urllib.parse import quote

cityname = "京都"

#url = 'https://www.google.co.jp/search'
#url = 'https://ja.wikipedia.org/wiki/'
#url = 'http://www.yahoo.co.jp'
url = "https://search.yahoo.co.jp/"
#search?p={}&n=60".format(quote(cityname))
#https://www.arukikata.co.jp/city/AMS/

resp = requests.get(url, params={'q': cityname})
print(resp.text)

resp.raise_for_status()

# 取得したHTMLをパースする
soup = bs4.BeautifulSoup(resp.text, "html.parser")

for aa in soup.find_all("a"):
            link = aa.get("href").replace('/url?q=','')
            name = aa.get_text()
            print(link,"\t",name)

print("aaa")

for aa in soup.find_all("p"):
            name = aa.get("cut3")
            print(name)

bb = soup.find_all("p", attrs={"class", "cut3"})
print(bb)



#print(soup)
# 検索結果のタイトルとリンクを取得
link_elem01 = soup.select('.r > a')
# 検索結果の説明部分を取得
link_elem02 = soup.select('.s > .st')

#print(link_elem01)

if(len(link_elem02) <= len(link_elem01)):
    leng = len(link_elem02)
else:
    leng = len(link_elem01)

#for i in range(leng):
#        # リンクのみを取得し、余分な部分を削除する
#        url_text = link_elem01[i].get('href').replace('/url?q=','')
#        # タイトルのテキスト部分のみ取得
#        title_text = link_elem01[i].get_text()
#        # 説明のテキスト部分のみを取得/余分な改行コードは削除する
#        t01 = link_elem02[i].get_text()
#        t02 = t01.replace('\n','')
#        disc_text = t02.replace('\r','')
#        print(title_text + disc_text,url_text)
