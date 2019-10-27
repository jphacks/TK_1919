import sys
import math
def sim_distance(user,city):
  sum_sqrt = 0
  for i in range(len(user)):
    sum_sqrt += (user[i] - city[i]) ** 2
  return 1/(1+sum_sqrt)


def tsv_input():
  args = sys.argv
  city_file = args[1]
  user_preference = args[2]
  with open(user_preference) as f:
    line = f.readline()
    user = list(map(int,line.split()))
    print(user)
  with open(city_file) as f:
    line = f.readline()
    cnt = 0
    sum_sqrt_list = []
    city = []
    city_vals = []
    city_list = []
    while line:
      if cnt == 0:
        name_eval = list(map(str,line.split()))
        print(name_eval)
        line = f.readline()
        pass # 先頭行
      cnt += 1
      city_info = list(map(str,line.split()))
      city_name = list(map(str,line.split()))[0]
      city_val = [int(s) for s in city_info[1:]]
      city_list.append(city_name)
      city_vals.append(city_val)
      #print(city_val)
      sum_sqrt_list.append(sim_distance(user,city_val))
      city.append(city_name)
      #print(preference_list)
      line = f.readline()
    print(city_list)
    sort_list = sorted(zip(city,city_vals))
    return(sort_list)
    
if __name__ == "__main__":
  print(tsv_input())


