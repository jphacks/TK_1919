
usrsen = [
["手軽さが好き","冒険心のある"],
["賑やかな場所が好き","落ち着いた場所"],
["半袖が好きな","コートが似合う"],
["教養深い","動物や植物が好き"],
["アジアに興味のある","洋風好み"]
]
citysen = [
["近場の","遠く離れた"],
["活気溢れる街","のどかな風景に囲まれた"],
["太陽が眩しい","爽やかな気候の"],
["歴史溢れる","大自然に囲まれた"],
["エスニックな雰囲気のある","欧米的な雰囲気の"]
]

def make_comment(data,city) :
    a = []
    for i in range(len(data)) :
        b = [data[i]]
        b.append(i)
        a.append(b)
    a.sort()
    str = usrsen[a[4][1]][0]+"で"+usrsen[a[0][1]][1]+"なあなたには、"+citysen[a[4][1]][0]+"で"+citysen[a[0][1]][1]+"な街であるこれらの都市がおすすめです。"
    return str


data = [3,5,2,4,2]
city = "東京"
print(make_comment(data,city))
