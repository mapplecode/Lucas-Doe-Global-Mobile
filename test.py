# import requests
# import json
# import pprint


# new_list=[]
# url = "https://api.verbwire.com/v1/nft/data/historicalStatsForSlug?slug=boredapeyachtclub&limit=25&offset=0&sortDirection=DESC"

# payload={}
# headers = {
#   'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
#   'accept': 'application/json'
# }
# response = requests.request("GET", url, headers=headers, data=payload)
# data=response.json()
# import pprint

# # pprint.pprint(data)
# res=data.get('historicalStats')
# print(res)
# for i in res:
#   eventType=i.get('eventType')
#   print(eventType,"+++++++++++++")
#   slug=i.get('slug')
#   contractId=i.get('contractId')
#   chain=i.get('chain')
#   floorSale=i.get('floorSale')
#   salesCount=i.get('salesCount')
#   rank=i.get('rank')
#   volume=i.get('volume')
#   total = slug,volume,salesCount,eventType,contractId,chain,floorSale,rank
#   print(total,"===")
 
#   new_list.append(total) 
# total=sorted(new_list)
# # print(total,"====")
# GetVolume = new_list[::-1][0:10]
# print(GetVolume,"+++++")




import requests
import json


def main(phone):
    """    repr :     
    """
    url = "https://devapi.endato.com/PersonSearch"

    payload = json.dumps({
    "Phone": phone
    })
    headers = {
    'galaxy-ap-name': 'f5778850-ab32-401e-bca1-377606919ae0',
    'galaxy-ap-password': '54e01deb091c4df2bef74481b5093453',
    'galaxy-search-type': 'Person',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("+++++++++++++++")
    return json.loads(response.text),response.status_code
main()
    
  
  