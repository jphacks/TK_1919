import sys
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

def tsv_input():
  args = sys.argv
  city_file = args[1]
  user_preference = args[2]
  with open(city_file) as f:
    line = f.readline()
    cnt = 0
    while line:
      if cnt == 0:
        name_eval = list(map(str,line.split()))
        print(name_eval)
        line = f.readline()
        pass # 先頭行
      cnt += 1
      #print(list(map(str,line.split())))
      city_info = list(map(str,line.split()))
      city_name = list(map(str,line.split()))[0]
      city_val = list(map(str,line.split()))[1:]
      city_dict = dict(zip(name_eval,city_val))
      print(city_dict)
      #print(preference_list)
      line = f.readline()

if __name__ == "__main__":
  tsv_input()


