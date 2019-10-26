import sys

if __name__ == '__main__':
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
        pass # 先頭行
      cnt += 1
      #print(line)
      #print(list(map(str,line.split())))
      city_info = list(map(str,line.split()))
      city_name = list(map(str,line.split()))[0]
      city_val = list(map(str,line.split()))[1:]
      city_dict = dict(zip(name_eval,city_val))
      print(city_dict)
      #print(preference_list)
      line = f.readline()
