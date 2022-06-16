from flask import Flask, render_template, url_for, request, redirect, session, Response, flash
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import getProducts, getProductById, getCart, Error
from cs50 import SQL

app = Flask(__name__)

# Connect DB:
db = SQL('sqlite:///test.db')

# Session Secret:
app.secret_key = "secret"

@app.route('/', methods=["GET"])
def index():
    if 'user' in session:
        return redirect('/main')

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

        return Response(status=200)
    else:
        if "user" not in session:
            return redirect('/')
        if "category" not in session:
            return redirect('/main')
        else:
            products = getProducts(session['category'])         
            return render_template('products.html', products=products)

@app.route('/cart', methods=["GET", "DELETE"])
def cart():
    cartIds = getCart()
    cart = []
    for item in cartIds:
        product = getProductById(item['product_id'])
        cart.append(product)

    return render_template('cart.html', cart=cart)

@app.route('/deleteCart', methods=["DELETE"])
def deleteCart():
    productId = request.args['id']
    
    if productId == 'all':
        db.execute(
            'DELETE FROM Products_User WHERE user_id = ?', session['user']
        )
    else:
        db.execute(
            'DELETE FROM Products_User WHERE user_id = ? AND product_id = ? LIMIT 1', session['user'], productId
        )

    return Response(status=200)
    
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get('username')
        password = request.form.get('password')
        verify = request.form.get('verify')

        if not username or not password or not verify:
            return Error(400, 'You must provide username, password and password verification')
        if password != verify:
            return Error(401, 'The password verification is not valid')

        rows = db.execute('SELECT * FROM Users WHERE username = ?', username)

        if len(rows) != 0:
            return Error(409, 'This username is not available')

        hash = generate_password_hash(password)
        
        db.execute(
            'INSERT INTO Users (username, password) VALUES (?, ?)', username, hash
            )

        flash('You have been registered!')
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
            return Error(400, 'You must provide username and password')

        user = db.execute(
            'SELECT * FROM Users WHERE username = ?', username
        )

        if len(user) == 0:
            return Error(401, 'Wrong credentials')

        if not check_password_hash(user[0]['password'], password):
            return Error(401, 'Wrong credentials')

        session['user'] = user[0]['id']

        flash('You have been logged in!')
        return redirect('/main')

    else:
        if "user" in session:
            flash('You are already logged in!')
            return redirect('/main')
        
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out!")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')