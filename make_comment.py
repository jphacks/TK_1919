

def make_comment(data,city) :
    usrsen = [
    ["手軽さが好きで","冒険心のある"],
    ["賑やかな場所が好きで","落ち着いた場所が好きな"],
    ["半袖が好きで","コートが似合う"],
    ["教養深く","動物や植物が好きな"],
    ["アジアに興味があり","洋風好みな"]
    ]
    citysen = [
    ["近場で","遠く離れた"],
    ["活気に溢れ","のどかな風景に囲まれた"],
    ["太陽が眩しく","寒さに試される"],
    ["歴史に溢れ","大自然に囲まれた"],
    ["エスニックな雰囲気のある","欧米的な雰囲気の"]
    ]
    a = []
    for i in range(len(data)) :
        b = [data[i]]
        b.append(i)
        a.append(b)
    a.sort()
    str = usrsen[a[4][1]][0]+usrsen[a[0][1]][1]+"あなたには、"+citysen[a[4][1]][0]+citysen[a[0][1]][1]+"これらの都市がおすすめです。"
    return str


data = [3,5,2,4,2]
city = "東京"
print(make_comment(data,city))
