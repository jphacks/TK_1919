import math

def sim_distance(prefs, person1, person2):
    # person1とperson2が共に評価してるもののリスト
    si = {}

    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # person1とperson2がどちらも評価してるものが無ければ類似性は0
    if len(si) == 0 :
        return 0

    # 各項目ごとの差の平方
    squares = [(prefs[person1][item] - prefs[person2][item]) ** 2 for item in si]
    sum_of_sqrt = math.sqrt(sum(squares))
    return 1/(1 + sum_of_sqrt)

def min_distance(usrdict,citydata) :
    #data = citydata
    #usrname = ["1","2","3"]
    cityname = ['Lisa Rose','Gene Seymour','Michael Phillips','Claudia Puig']
    #usrdata_dict = []
    #usrdata_dict[0] = dict(zip(usrname,usrvec)
    #usrdict = dict(zip(["usr"],usrdata_dict))

    #data = [[1,2,3],[2,3,4],[3,4,5]]
    #dic1 = []*len(data)
    citydata.update(usrdict)
    data = citydata
    
    for citynum in range(len(cityname)) :
        r = sim_distance(data, 'Toby', cityname[citynum])
    return r



critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.5,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
}
usr = {'Toby': {
    'Snakes on a Plane': 4.5,
    'You, Me and Dupree': 1.0,
    'Superman Returns': 4.0,
}}
#usrdict = {"usr":{"1":1,"2":2,"3":3}
#citydata = {"a":{"1":2,"2":3,"3":4},"b":{"1":3,"2":4,"3":5}}
data = min_distance(usr,critics)
print(data)
