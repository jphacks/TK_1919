import requests
import json

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"
APIKey = "c92d3c4eecmshb37fe7ee2e6c5eap106f08jsn556a682992c3"

headers={
    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "X-RapidAPI-Key": APIKey,
    "Content-Type": "application/x-www-form-urlencoded"
}

params={
    "inboundDate": "2019-09-10",
    "cabinClass": "business",
    "children": 0,
    "infants": 0,
    "country": "US",
    "currency": "USD",
    "locale": "en-US",
    "originPlace": "SFO-sky",
    "destinationPlace": "LHR-sky",
    "outboundDate": "2019-09-01",
    "adults": 1
}

req = requests.post(url,data=json.dumps(params),headers=headers)

req.raise_for_status()

print(req.status_code)