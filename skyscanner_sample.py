import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"
APIKey = "c92d3c4eecmshb37fe7ee2e6c5eap106f08jsn556a682992c3"

payload = "country=US&currency=USD&locale=en-US&originPlace=SFO-sky&destinationPlace=LHR-sky&outboundDate=2019-12-01&adults=1"
headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': APIKey,
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.status_code)
print(response.headers)

r = response.headers
r = r['Location']
r = r.split('/')
sessionkey = r[-1]

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/"+sessionkey

querystring = {"pageIndex":"0","pageSize":"10"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "c92d3c4eecmshb37fe7ee2e6c5eap106f08jsn556a682992c3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

path_w = 'skyscannerresult.txt'
with open(path_w, mode='a') as f:
    f.write(response.text)
#print(url)
#print(response.text)
