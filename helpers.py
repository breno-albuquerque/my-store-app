import os
import requests

API_URL = 'https://api.mercadolibre.com/sites/MLB/search?q=monitor'
products = []

def getProducts():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        
        for i in range(len(data['results'])):
            if i <= 50:
                products.append(data['results'][i])

        return products        

    except Exception as e:
        print(e)
        return None
