from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Config DB:
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Initialize DB:
db = SQLAlchemy(app)
# Create DB Model:
class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')