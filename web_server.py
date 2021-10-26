import os
from flask import Flask, render_template, request, url_for, redirect
from flask.globals import session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI2')

mongo = PyMongo(app)

users = mongo.db.users
loans = mongo.db.loans

@app.route("/")
def index():
    if 'username' in session:
        return 'You are logged in as following user: ' + session['username']
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    login_user = users.find_one({"username" : request.form['username']})
    print(login_user)
    if login_user:
        # if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
        if request.form['pass']==login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return 'Invalid username or password combination'

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method =='POST':
        existing_user =  users.find_one({'username': request.form['username']})

        if existing_user is None:
            # hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username': request.form['username'], 'password': request.form['pass']})
            session['username']= request.form['username']
            return redirect(url_for('index'))
    
        return 'Username already exists'
    return render_template('register.html')


if (__name__ == '__main__'):
    app.secret_key='secretivekey'
    app.run(debug=True)