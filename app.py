from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request
from mail_send import mail_send
import os

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:zayyad@localhost/postgres'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Productcat(db.Model):
    __tablename__ : 'productcat'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    marketer = db.Column(db.String(200))
    product = db.Column(db.String(200))
    size = db.Column(db.String(5))
    
    def __init__(self,customer, marketer, product, size):
        self.customer = customer
        self.marketer = marketer
        self.product = product
        self.size = size
        
@app.route('/', methods=['GET', 'POST'])
def index():
        return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        marketer = request.form['marketer']
        product = request.form['product']
        size = request.form['size']
        #print(customer,dealer,rating,comments)
        if customer == '' or marketer == '':
            return render_template('index.html', message='Please Enter Required  fields')
        if db.session.query(Productcat).filter(Productcat.customer == customer).count() == 0:
            data = Productcat(customer, marketer, product, size)
            db.session.add(data)
            db.session.commit()
            mail_send(customer, marketer, product, size)
        return render_template('success.html')
         


if __name__ == '__main__':
    app.run()