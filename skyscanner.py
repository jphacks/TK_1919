import requests
import json
import urllib

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"
APIKey = "c92d3c4eecmshb37fe7ee2e6c5eap106f08jsn556a682992c3"

headers={
    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "X-RapidAPI-Key": APIKey,
    "Content-Type": "application/x-www-form-urlencoded"
}

params={
    "country": "US",
    "currency": "USD",
    "locale": "en-US",
    "originPlace": "SFO-sky",
    "destinationPlace": "LHR-sky",
    "outboundDate": "2019-12-01",
    "adults": 1
}

req = requests.post(url,data = params,headers=headers)

print(req.status_code)
req.raise_for_status()

urllib.request.urlopen(req)

#r = req.headers
#print(r)
#print(r['Location'])

#headers={
#    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
#    "X-RapidAPI-Key": APIKey,
#    "Content-Type": "application/json"
#}

#q = requests.post(r['Location'],headers = headers)

#print(q)