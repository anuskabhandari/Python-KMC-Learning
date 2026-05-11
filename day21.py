import requests

url = "https://markets.onlinekhabar.com/smtm/home/sector-performance"

r = requests.get(url=url)# keyword arg liyeko
if r.status_code ==200:
    data = r.json() ['response'] # response key hoo vnera find out gareko using data.keys()
    for i in data:
        print(i['indices'] , i ['percentage_change'])
    
else:
    print("Fail")    


