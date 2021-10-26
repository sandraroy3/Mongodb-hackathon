import os
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI2')
# set env var MONGO_URI2 to 'mongodb+srv://admin:admin@hackathon.qd2rc.mongodb.net/bank?retryWrites=true&w=majority&authSource=admin'

mongo = PyMongo(app)

users = mongo.db.users

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/register')
def register_user():
    # saved_users = users.find()
    return render_template('register.html')
    # new_user = request.form.get('new-user')
    # users.insert_one({'text' : new_user, 'complete' : False})
    # return redirect(url_for('index'))

@app.route('/login')
def login_user():
    # saved_users = users.find()
    return render_template('login.html')
  

# @app.route('/users')
# def complete(oid):
#     user_item = users.find_one({'_id': ObjectId(oid)})
#     user_item['complete'] = True
#     users.save(user_item)
#     return redirect(url_for('index'))

# @app.route('/delete_completed')
# def delete_completed():
#     todos.delete_many({'complete' : True})
#     return redirect(url_for('index'))

# @app.route('/delete_all')
# def delete_all():
#     todos.delete_many({})
#     return redirect(url_for('index'))

# if __name__ == "__main__":
#     app.run()