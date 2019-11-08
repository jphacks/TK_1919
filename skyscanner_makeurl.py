import webbrowser
import datetime

params={
    "inboundDate": "2019-09-10",
    "cabinClass": "business",
    "children": 0,
    "infants": 0,
    "country": "US", #ここから下が必須データ
    "currency": "USD",
    "locale": "en-US",
    "originPlace": "SFO",
    "destinationPlace": "LHR",
    "outboundDate": str(datetime.date.today()),
    "adults": 1
}

url = 'https://www.skyscanner.jp/transport/flights/'+params['originPlace']+'/'+params['destinationPlace']+'/'+params['outboundDate']+'/?adultsv2=1/'

print(url)

webbrowser.open(url,1)