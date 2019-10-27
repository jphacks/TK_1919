import json
import math
from urllib.parse import quote

# city value of each collum
col_name = ['近さ', '都会さ', '暑さ', '文化的', '東洋的']
city_val = [('アムステルダム', [1, 3, 2, 2, 1]), ('エジプト', [2, 2, 4, 5, 3]), ('ジャカルタ', [3, 3, 4, 2, 4]), ('セブ', [3, 1, 3, 1, 3]), ('ソウル', [4, 3, 3, 3, 4]), ('チューリッヒ', [1, 2, 1, 2, 1]), ('テキサス', [2, 1, 3, 1, 1]), ('ニューヨーク', [1, 5, 1, 4, 2]), ('ハノイ', [3, 2, 3, 3, 2]), ('バンコク', [3, 3, 4, 3, 3]), ('パリ', [1, 4, 2, 4, 2]), ('ベルリン', [1, 3, 1, 3, 1]), ('ホノルル', [3, 2, 4, 1, 3]), ('ロンドン', [1, 4, 1, 4, 4]), ('上海', [4, 3, 3, 3, 4]), ('京都', [5, 3, 3, 5, 5]), ('北京', [4, 4, 4, 4, 5]), ('北海道', [4, 1, 1, 1, 3]), ('東京', [5, 5, 4, 3, 4]), ('沖縄', [4, 2, 4, 1, 4])]
minor_city_val = [('アルバニア', [1, 3, 3, 2, 1]), ('アルメニア', [2, 3, 3, 4, 1]), ('イラン', [2, 2, 4, 2, 2]), ('ウズベキスタン', [2, 2, 4, 2, 2]), ('キルギス', [2, 2, 3, 3, 2]), ('クロアチア', [1, 3, 2, 3, 1]), ('ジョージア', [1, 2, 3, 4, 1]), ('トルクメニスタン', [2, 1, 4, 2, 2]), ('ハンガリー', [1, 3, 2, 1, 1]), ('伊豆諸島(東京)', [3, 1, 3, 3, 4]), ('岡山', [3, 2, 2, 1, 2]), ('長崎', [3, 2, 3, 1, 2]), ('長野', [4, 2, 2, 2, 3]), ('静岡', [4, 3, 2, 2, 2])]


def sim_distance(user,city):
  sum_sqrt = 0
  for i in range(len(user)):
    sum_sqrt += (user[i] - city[i]) ** 2
  return 1/(1+sum_sqrt)


def choose_min3_city(user):
   similarity = []
   for i in range(len(city_val)):
    similarity.append([sim_distance(user,city_val[i][1]),city_val[i][0],city_val[i][1]])
   #print(similarity)
   sort_sim = sorted(similarity)
   best_3 = sort_sim[-3:]
   worst = sort_sim[0]
   best_3.append(worst)
   similarity_minor = []
   for i in range(len(minor_city_val)):
    similarity_minor.append([sim_distance(user,minor_city_val[i][1]),minor_city_val[i][0],minor_city_val[i][1]])
   sort_sim_minor = sorted(similarity_minor)
   best_3_minor = sort_sim_minor[-3:]
   worst_minor = sort_sim_minor[0]
   best_3.extend(best_3_minor)
   best_3.append(worst_minor)
   return(best_3)

def lambda_handler(event, context):
    # TODO implement
    user = event['array']#listで受け取り
    print (choose_min3_city(user))
    
    return {
        'statusCode': 200,
        'body': choose_min3_city(user)
    }
