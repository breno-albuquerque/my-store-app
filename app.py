from flask import Flask, render_template, url_for, request, redirect
from helpers import getProducts
from cs50 import SQL

app = Flask(__name__)

# Initialize DB:
db = SQL('sqlite:///test.db')

@app.route('/')
def index():
    products = getProducts()
    return render_template('layout.html', products=products)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        name = request.form.get('username')
        password = request.form.get('password')

        db.execute(
            'INSERT INTO Users (username, password) VALUES (?, ?)', name, password
            )

        return redirect('/')

    else:
        return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        username = request.form.get('username')
        password = request.form.get('password')

        user = db.execute(
            'SELECT username, password FROM Users WHERE username = ?', username
        )

        if user[0]['password'] != password:
            return print('Senha incorreta')

        return redirect('/')

    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')