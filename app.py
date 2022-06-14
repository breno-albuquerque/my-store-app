from flask import Flask, render_template, url_for, request, redirect, session
from helpers import getProducts
from cs50 import SQL

app = Flask(__name__)

# Initialize DB:
db = SQL('sqlite:///test.db')

# Session Secret:
app.secret_key = "secret"

@app.route('/')
def index():
    # Need to check if is logged in
    return render_template('home.html')

@app.route('/products')
def home():
    if "user" in session:

        user = session["user"]
        products = getProducts()
        return render_template('products.html', products=products)
    
    else:
        return redirect('/')
    
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        name = request.form.get('username')
        password = request.form.get('password')
        verify = requires.form.get('verify')

        if not name or not password or not verify:
            return print('Every input must be provided')
        if password != verify:
            return print('The password verification is not valid')

        rows = db.execute('SELECT * FROM Users WHERE username = ?', username)

        if len(rows) != 0:
            return print('This username is not available')
        
        db.execute(
            'INSERT INTO Users (username, password) VALUES (?, ?)', name, password
            )

        return redirect('/')

    else:
        # Need to check if is logged in

        return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return prin('Every input must be provided')

        user = db.execute(
            'SELECT * FROM Users WHERE username = ?', username
        )

        if user[0]['password'] != password:
            return print('Senha incorreta')

        # Set Session:
        session['user'] = user[0]['id']

        return redirect('/products')

    else:
        if "user" in session:
            return redirect('/products')
        
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')