import os
from flask import Flask, render_template, request, url_for, redirect
from flask.globals import session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
import time
import tkinter as tk
from tkinter import ttk

NORM_FONT= ("Verdana", 10)

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI2')

mongo = PyMongo(app)

users = mongo.db.users
loans = mongo.db.loans

@app.route("/", methods=['POST', 'GET'])
def base():
    return render_template('base.html')

@app.route("/logged")
def logged():
    if 'username' in session:
        return render_template('apply.html')
    return render_template("index.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    login_user = users.find_one({"username" : request.form['username']})
    print(login_user)
    if login_user:
        # if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
        if request.form['pass']==login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('logged'))
    return 'Invalid username or password combination'

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method =='POST':
        existing_user =  users.find_one({'username': request.form['username']})

        if existing_user is None:
            # hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username': request.form['username'], 'password': request.form['pass']})
            session['username']= request.form['username']
            return redirect(url_for('base'))
    
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
        # return redirect(url_for('base'))
      
    return render_template('apply.html')


@app.route('/update_status', methods=['POST'])
def update_status(income):
    if request.method =='POST':
        if int(income) > 50000:
            users.update_one({'username': session['username']},
                            {"$set": {'loan_status': 'Aproved'}})
            print("You are approved.")
        elif int(income) <= 50000:
            users.update_one({'username': session['username']},
                            {"$set": {'loan_status': 'DENIED'}})
            print("You are Denied.")
    return render_template('base.html')

# def popupmsg(msg):
#     popup = tk.Tk()
#     popup.wm_title("!")
#     label = ttk.Label(popup, text=msg, font=NORM_FONT)
#     label.pack(side="top", fill="x", pady=10)
#     B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
#     B1.pack()
#     popup.mainloop()

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('base'))

if (__name__ == '__main__'):
    app.secret_key='secretivekey'
    app.run(debug=True)