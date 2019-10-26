
import json
#from botocore.vendored import requests #AWS用
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
    #j = json.loads(r.text.decode('utf-8'))

    return r.text


if __name__ == "__main__":

    j = gooAPIkeyword( "TWA85: 'The world's longest and most spectacular hijacking'" , "Under the hills of southern Italy, a little north-east of Naples, a fault ruptured and the earth began shaking. Those living on the surface, in one of the most earthquake-prone parts of Europe, were used to this. The 6.1-magnitude quake in the early evening was enough to frighten everyone, but it was the two powerful aftershocks that did the most damage.Twenty kilometres up from the epicentre and a few hundred metres north was where the Minichiello family lived, including 12-year-old Raffaele. By the time the third earthquake had subsided, their village of Melito Irpino was uninhabitable. The Minichiello family were left with nothing, Raffaele would later recall, and no-one in authority came to help.The damage was such that almost the entire village was evacuated, razed and rebuilt. Many families would return, but the Minichiellos decided to move to the US for a better life.What Raffaele Minichiello found instead was war, trauma and notoriety." ,3)

    #k = j["keywords"]
    #l = k[0]
    print(j);
