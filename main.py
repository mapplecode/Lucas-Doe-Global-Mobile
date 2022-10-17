# import requests
# import json


new_list ={}
def holder(request):
  url = "https://api.verbwire.com/v1/nft/data/historicalStatsForSlug?slug=boredapeyachtclub&limit=25&offset=0&sortDirection=DESC"
  payload={}
  headers = {
    'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
    'accept': 'application/json'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  data=response.json()
  res=data.get('historicalStats')
  data = [i.get('volume') for i in res ]
  Output = sorted(data, key = lambda x:float(x))[::-1]
  emp = list()
  for i in Output:
    if i not in emp:
      emp.append(i)
  getTopVolume = emp[:10]
  print(getTopVolume)
    
    
    