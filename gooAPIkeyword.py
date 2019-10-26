
import json
from botocore.vendored import requests #AWS用
import requests #AWS以外用

method = "POST"
headers = {"Content-Type" : "application/json"}
appID = "b664516431b4a1264f36746219a8bcbee9a7f807d6af52373ed3add943af0d3a"

def gooAPIkeyword(s_title,s_body,max_num) :

    url = "https://labs.goo.ne.jp/api/keyword"

    obj = {"app_id":appID,"request_id":"record001","title":s_title,"body":s_body,"max_num":max_num,"focus":"ORG"}
    json_data = json.dumps(obj).encode("utf-8")

    proxies = []
    params = {}
    headers = {'Content-Type' : 'application/json'}
    r = requests.post(url, params=params, data=json_data, headers=headers, proxies=proxies, timeout=10)
    j = json.loads(r.text.decode('utf-8'))

    return j


if __name__ == "__main__":

    j = gooAPIkeyword( "「和」をコンセプトとする 匿名性コミュニケーションサービス「MURA」 gooラボでのβ版のトライアル実施 ～gooの検索技術を使った「ネタ枯れ防止機能」によりコミュニティの話題活性化が可能に～" , "NTTレゾナント株式会社（本社：東京都港区、代表取締役社長：若井 昌宏、以下、NTTレゾナント）は、同じ興味関心を持つ人と匿名でコミュニティをつくることができるコミュニケーションサービス「MURA」を、2015年8月27日よりgooラボ上でβ版サイトのトライアル提供を開始します。" ,3)

    #k = j["keywords"]
    #l = k[0]
    print(j);
