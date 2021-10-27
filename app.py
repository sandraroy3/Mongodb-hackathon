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
        return render_template("apply.html")
    return render_template("index.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    login_user = users.find_one({"username" : request.form['username']})
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

@app.route('/update', methods=['POST'])
def update_user():
    if request.method =='POST':
        users.update_one({'username': session['username']},
                         {"$set": {'name': request.form['name'],
                         'income': request.form['income'],
                         'address': request.form['address']}})
        update_status(request.form['income'])
        return redirect(url_for('index'))
    return render_template('apply.html')


@app.route('/update_status', methods=['POST'])
def update_status(income):
    if request.method =='POST':
        if int(income) > 50000:
            users.update_one({'username': session['username']},
                            {"$set": {'loan_status': 'Aproved'}})
            return 'You are approved: ' + session['username']
        elif int(income) <= 50000:
            users.update_one({'username': session['username']},
                            {"$set": {'loan_status': 'DENIED'}})
            return 'You are denied: ' + session['username']
    return render_template('base.html')


# @app.route('/delete_completed_application')
# def delete_completed():
#     '''Deletes all the user applications marked complete'''
#     users.applications.delete_many({'complete' : True})
#     return redirect(url_for('index'))


if (__name__ == '__main__'):
    app.secret_key='secretivekey'
    app.run(debug=True)