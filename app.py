from flask import Flask, render_template, url_for, request, redirect, session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import getProducts, getProductById
from cs50 import SQL

app = Flask(__name__)

# Initialize DB:
db = SQL('sqlite:///test.db')

# Session Secret:
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/main', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        category = request.form.get('category')

        session['category'] = category

        return redirect('/products')
    else:    
        if 'user' in session:
            return render_template('main.html')
        return redirect('/login')


@app.route('/products', methods=["GET", "POST"])
def home():
    if request.method == "POST":

        productId = request.json['productId']
        product = getProductById(productId)[0]['body']

        rows = db.execute(
            'INSERT INTO Products_User (product_id, user_id) VALUES (?, ?)', productId, session['user']
        )

        products = db.execute(
            'SELECT product_id FROM Products_User WHERE user_id = ?', session['user']
        )

        session['cart'] = products

        return redirect('/')

    else:

        if "user" in session:
    
            user = session["user"]
            products = ''

            if "category" in session:
                products = getProducts(session['category'])
            else:
                products = getProducts('desktop')

            if "cart" in session:
                
                cart = session["cart"]
                cartProducts = []

                for i in cart:
                    product = getProductById(i['product_id'])
                    cartProducts.append(product)           

                return render_template('products.html', products=products, cartProducts=cartProducts)

            return render_template('products.html', products=products)
        else:
            return redirect('/')
    
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get('username')
        password = request.form.get('password')
        verify = request.form.get('verify')

        if not username or not password or not verify:
            return print('Every input must be provided')
        if password != verify:
            return print('The password verification is not valid')

        rows = db.execute('SELECT * FROM Users WHERE username = ?', username)

        if len(rows) != 0:
            return print('This username is not available')

        hash = generate_password_hash(password)
        
        db.execute(
            'INSERT INTO Users (username, password) VALUES (?, ?)', username, hash
            )

        return redirect('/')

    else:
        if "user" in session:
            return redirect('/logout')
        
        return render_template('register.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return print('Every input must be provided')

        user = db.execute(
            'SELECT * FROM Users WHERE username = ?', username
        )

        if not check_password_hash(user[0]['password'], password):
            return print('Senha incorreta')

        # Set Session user:
        session['user'] = user[0]['id']

        products = db.execute(
            'SELECT product_id FROM Products_User WHERE user_id = ?', session['user']
        )

        #Set Session cart:
        if len(products) != 0:
            session['cart'] = products

        return redirect('/home')

    else:
        if "user" in session:
            return redirect('/products')
        
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("user", None)
    session.pop("cart", None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')