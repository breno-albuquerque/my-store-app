import os
import requests

from flask import session, render_template
from cs50 import SQL

db = SQL('sqlite:///test.db')

def getProducts(category):
    products = []

    try:
        response = requests.get(f'https://api.mercadolibre.com/sites/MLB/search?q={category}')
        response.raise_for_status()
        data = response.json()
        
        for i in range(len(data['results'])):
            if i <= 20:
                products.append(data['results'][i])

        return products

    except Exception as e:
        print(e)
        return None
    
def getProductById(id):
    try:
        response = requests.get(f'https://api.mercadolibre.com/items?ids={id}')
        response.raise_for_status()
        data = response.json()

        return data
    
    except Exception as e:
        print(e)
        return None

def Error(code, message):
    return render_template('error.html', code=code, message=message)


def getCart():
    return db.execute(
        'SELECT product_id FROM Products_User WHERE user_id = ?', session['user']
    )
