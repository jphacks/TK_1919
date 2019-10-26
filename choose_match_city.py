import sys
import math
user = [1,1,1,1,1]#listで受け取り
# city value of each collum

col_name = ['近さ', '都会さ', '暑さ', '文化的', '東洋的']
city_val = [('アムステルダム', [1, 3, 2, 2, 1]), ('エジプト', [2, 2, 4, 5, 3]), ('ジャカルタ', [3, 3, 4, 2, 4]), ('セブ', [3, 1, 3, 1, 3]), ('ソウル', [4, 3, 3, 3, 4]), ('チューリッヒ', [1, 2, 1, 2, 1]), ('テキサス', [2, 1, 3, 1, 1]), ('ニューヨーク', [1, 5, 1, 4, 2]), ('ハノイ', [3, 2, 3, 3, 2]), ('バンコク', [3, 3, 4, 3, 3]), ('パリ', [1, 4, 2, 4, 2]), ('ベルリン', [1, 3, 1, 3, 1]), ('ホノルル', [3, 2, 4, 1, 3]), ('ロンドン', [1, 4, 1, 4, 4]), ('上海', [4, 3, 3, 3, 4]), ('京都', [5, 3, 3, 5, 5]), ('北京', [4, 4, 4, 4, 5]), ('北海道', [4, 1, 1, 1, 3]), ('東京', [5, 5, 4, 3, 4]), ('沖縄', [4, 2, 4, 1, 4])]
def sim_distance(user,city):
  sum_sqrt = 0
  for i in range(len(user)):
    sum_sqrt += (user[i] - city[i]) ** 2
  return 1/(1+sum_sqrt)


def choose_min3_city():
   similarity = []
   for i in range(len(city_val)):
    similarity.append([sim_distance(user,city_val[i][1]),city_val[i][0],city_val[i][1]])
   #print(similarity)
   min_3 = sorted(similarity)[:3]
   return(min_3)
      
if __name__ == "__main__":
  print(choose_min3_city())


