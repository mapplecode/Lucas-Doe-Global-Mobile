import requests
import json
from datetime import datetime

# url = "https://api.verbwire.com/v1/nft/data/salesEventsForSlug?slug=boredapeyachtclub&chain=ethereum&limit=25&offset=0&sortDirection=DESC"

# payload={}
# headers = {
#   'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
#   'accept': 'application/json'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# data=json.loads(response.text)
# res=data.get('sales')
# for i in res:
#     a=i.get('sale')
#     # print(a)
#     b=i.get('timestamp')
    
#     print(b)


# num=[]
# url = "https://api.verbwire.com/v1/nft/data/historicalStatsForSlug?slug=boredapeyachtclub&chain=ethereum&limit=25&offset=0&sortDirection=DESC"

# payload={}
# headers = {
#   'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
#   'accept': 'application/json'
# }
# response = requests.request("GET", url, headers=headers, data=payload)
# data=json.loads(response.text)
# res=data.get('historicalStats')
# for i in res:
#   eventType=i.get('eventType')
#   slug=i.get('slug')
#   contractId=i.get('contractId')
#   chain=i.get('chain')
#   floorSale=i.get('floorSale')
#   salesCount=i.get('salesCount')
#   rank=i.get('rank')
#   volume=i.get('volume')
#   total = slug,volume,salesCount,eventType,contractId,chain,floorSale,rank
#   print(total,"===")

#   num.append(volume) 
# num.sort(key = float)
# GetVolume = num[::-1][0:10]
# # print(GetVolume,"====")


import requests

url = "https://api.verbwire.com/v1/nft/data/collections/all?chain=ethereum&limit=10&page=1&sortField=volume&sortInterval=allTime&sortDirection=ASC"

payload={}
headers = {
  'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
  'accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
data=json.loads
print(response.text)


# def holder(request):
#   print("===================")
#   url = "https://api.verbwire.com/v1/nft/data/historicalStatsForSlug?slug=boredapeyachtclub&limit=25&offset=0&sortDirection=DESC"
#   payload={}
#   headers = {
#     'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
#     'accept': 'application/json'
#   }
#   response = requests.request("GET", url, headers=headers, data=payload)
#   data=response.json()
#   res=data.get('historicalStats')
#   volume = [i.get('volume') for i in res ]
#   floorSale = [i.get('floorSale') for i in res ]
#   chain = [i.get('chain') for i in res]
#   slug = [i.get('slug') for i in res]
#   rank = [i.get('rank') for i in res]


#   Output = sorted(volume, key=lambda x:float(x))[::-1]
#   Output1 = sorted(floorSale, key=lambda x:float(x))[::-1]
#   emp = list()
#   emp1 = list()
#   for i in Output:
#     if i not in emp:
#       emp.append(i)
#   getTopVolume = emp[:10]
#   for v in Output1:
#     if v not in emp1:
#       emp1.append(v)
#   getTopVolume1 = emp1[:10]

#   chain.sort()
#   slug.sort()
#   rank.sort(key=int)

#   getChain = chain[:10][::-1] 
#   getslug=slug[:10][::-1]
#   getrank=rank[:10][::-1]

#   context={
#   "getTopVolume":getTopVolume,
#   "getTopVolume1":getTopVolume1,
#   "getChain":getChain,
#   "getslug":getslug,
#   "getrank":getrank
#     }
  



#   return render(request,'index.html',context)  
    
    