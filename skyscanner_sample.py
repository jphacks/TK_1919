import requests
import webbrowser
import datetime

def skyscanner(city) :
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"
    APIKey = "c92d3c4eecmshb37fe7ee2e6c5eap106f08jsn556a682992c3"

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': APIKey,
        'content-type': "application/x-www-form-urlencoded"
    }

    airportdata = {"US" : "SFO","UK" : "LHR"}
    airport = airportdata[city]

    params={
        "country": "JP",
        "currency": "JPY",
        "locale": "en-US",
        "originPlace": "HND-sky",
        "destinationPlace": airport+"-sky",
        "outboundDate": str(datetime.date.today()),
        "adults": 1
    }

    response = requests.request("POST", url, data=params, headers=headers)
    s = str(response.status_code)
    if s[0] == '2' :
        r = response.headers
        r = r['Location']
        r = r.split('/')
        sessionkey = r[-1]
        return skyscanner_data(sessionkey)
    else :
        return []

def skyscanner_data(sessionkey) :
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/"+sessionkey

    querystring = {"pageIndex":"1","pageSize":"1"}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "c92d3c4eecmshb37fe7ee2e6c5eap106f08jsn556a682992c3"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response = response.json()
    r = response['Itineraries']
    if len(r)>0 :
        r = r[0]
        r = r['PricingOptions']
        r = r[0]
        price = r['Price']
        link = r['DeeplinkUrl']
        return [price,link]
    else :
        return []
    


city = "UK"
print(skyscanner(city))