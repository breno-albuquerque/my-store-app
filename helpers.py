import os
import requests

API_URL = 'https://api.mercadolibre.com/sites/MLB/search?q=monitor'

def getProducts():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        print(data)
    except requests.RequestException as e:
        print(e)


