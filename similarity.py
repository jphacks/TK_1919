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


def sim_pearson(prefs, person1, person2):
    si = {}

    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    n = len(si)

    if n == 0: return 0

    mean1 = sum([prefs[person1][item] for item in si]) / n
    mean2 = sum([prefs[person2][item] for item in si]) / n
    variance1 = math.sqrt(sum([((prefs[person1][item] - mean1) ** 2) for item in si]))
    variance2 = math.sqrt(sum([((prefs[person2][item] - mean2) ** 2) for item in si]))

    covariance = sum([(prefs[person1][item] - mean1)*(prefs[person2][item] - mean2) for item in si])

    if variance1 * variance2 == 0: return 0

    return covariance / (variance1 * variance2)
