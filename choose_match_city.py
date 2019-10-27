import sys
import math
distify_threshould = 20

user = [[5,4,3,4,5],[3,4,5,5,5],[3,3,4,4,5],[1,1,1,1,1]]#listで受け取り
# city value of each collum

col_name = ['近さ', '都会さ', '暑さ', '文化的', '東洋的']
major_city_val = [('アムステルダム', [1, 3, 2, 2, 1]), ('エジプト', [2, 2, 4, 5, 3]), ('ジャカルタ', [3, 3, 4, 2, 4]), ('セブ', [3, 1, 3, 1, 3]), ('ソウル', [4, 3, 3, 3, 4]), ('チューリッヒ', [1, 2, 1, 2, 1]), ('テキサス', [2, 1, 3, 1, 1]), ('ニューヨーク', [1, 5, 1, 4, 2]), ('ハノイ', [3, 2, 3, 3, 2]), ('バンコク', [3, 3, 4, 3, 3]), ('パリ', [1, 4, 2, 4, 2]), ('ベルリン', [1, 3, 1, 3, 1]), ('ホノルル', [3, 2, 4, 1, 3]), ('ロンドン', [1, 4, 1, 4, 4]), ('上海', [4, 3, 3, 3, 4]), ('京都', [5, 3, 3, 5, 5]), ('北京', [4, 4, 4, 4, 5]), ('北海道', [4, 1, 1, 1, 3]), ('東京', [5, 5, 4, 3, 4]), ('沖縄', [4, 2, 4, 1, 4])]
minor_city_val = [('アルバニア', [1, 3, 3, 2, 1]), ('アルメニア', [2, 3, 3, 4, 1]), ('イラン', [2, 2, 4, 2, 2]), ('ウズベキスタン', [2, 2, 4, 2, 2]), ('キルギス', [2, 2, 3, 3, 2]), ('クロアチア', [1, 3, 2, 3, 1]), ('ジョージア', [1, 2, 3, 4, 1]), ('トルクメニスタン', [2, 1, 4, 2, 2]), ('ハンガリー', [1, 3, 2, 1, 1]), ('伊豆諸島(東京)', [3, 1, 3, 3, 4]), ('岡山', [3, 2, 2, 1, 2]), ('長崎', [3, 2, 3, 1, 2]), ('長野', [4, 2, 2, 2, 3]), ('静岡', [4, 3, 2, 2, 2])]
def sim_distance(user,city):
  sum_sqrt = 0
  for i in range(len(user)):
    sum_sqrt += (user[i] - city[i]) ** 2
  return 1/(1+sum_sqrt)
# だれもが大きな不満を抱かないように、(各個人の誤差の二乗の和+1)のグループ全体での逆数の和が最大になるようにする
# 特定の人の不満がdistify_threshould を超えた場合にはアラートを出す
def group_satisfaction(user,city):
  group_distify = 0
  cnt = 0
  distify_member = []
  for user_name in user:
    cnt += 1
    distify = 0
    for j in range(len(user_name)):
      distify += (user_name[j] - city[j])**2
      if j == len(user_name)-1:
        if distify >= distify_threshould:
          distify_member.append(cnt)
          #print(cnt, "番目さんは不満を抱いている可能性があります。仲違いするかも？！変更した方がいいかもしれません")
        group_distify += distify
  #print((group_distify,distify_member))
  return((group_distify,distify_member))


def choose_best3_worst_city(city_val):
   similarity = []
   for i in range(len(city_val)):
    distify_val,distify_member = group_satisfaction(user,city_val[i][1])
    similarity.append([distify_val,distify_member,city_val[i][0],city_val[i][1]])
   #print(similarity)
   sort_sim = sorted(similarity)
   best_3 = sort_sim[:3]
   worst = sort_sim[-1]
   best_3.append(worst)
   return(best_3)
      
if __name__ == "__main__":
  print(choose_best3_worst_city(major_city_val))
  print(choose_best3_worst_city(minor_city_val))


