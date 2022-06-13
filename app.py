from flask import Flask, render_template, url_for
from helpers import getProducts
from cs50 import SQL

app = Flask(__name__)

# Initialize DB:
db = SQL('sqlite:///test.db')

@app.route('/')
def index():
    products = getProducts()
    print(products)
    return render_template('layout.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')