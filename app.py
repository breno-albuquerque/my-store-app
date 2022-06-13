from flask import Flask, render_template, url_for, request
from helpers import getProducts
from cs50 import SQL

app = Flask(__name__)

# Initialize DB:
db = SQL('sqlite:///test.db')

@app.route('/')
def index():
    products = getProducts()
    return render_template('layout.html', products=products)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return None
    else:
        return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return None
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')