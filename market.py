import requests

url = "https://markets.onlinekhabar.com/smtm/home/most-searched-stocks"
r = requests.get(url=url)
if r.status_code == 200:
    data = r.json() ['response']
    for i in data:
        print(i['ticker'], i['no_of_hits'])
else:
    print("Fail") # type check gardai loop lagaudai print garne

#  inspect ma gayera network ma herera response ma dictinary jsto value xa vne matrai r.json use garna milxa