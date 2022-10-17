from dataclasses import dataclass
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
import json

def index(request):
  return render(request,'index.html')


def holder(request):
  url = "https://api.verbwire.com/v1/nft/data/historicalStatsForSlug?slug=boredapeyachtclub&limit=25&offset=0&sortDirection=DESC"
  payload={}
  headers = {
    'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
    'accept': 'application/json'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  data=response.json()

  
  res=data.get('historicalStats')[::-1][0:10]
  
  
  return render(request,'holder.html',{"form":res})



def collections(request):
  url = "https://api.verbwire.com/v1/nft/data/collections/all?chain=ethereum&limit=10&page=1&sortField=volume&sortInterval=allTime&sortDirection=ASC"

  payload={}
  headers = {
    'X-API-Key': 'sk_live_d1990002-2fbf-45c0-8430-264d1fa0a5b1',
    'accept': 'application/json'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  data=response.json()
  resp=data.get('collections').get('results')[::-1][0:10]
  return render(request,'collection.html',{"form":resp})







  