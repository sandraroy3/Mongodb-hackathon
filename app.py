import os
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI2')
# set env var MONGO_URI2 to 'mongodb+srv://admin:admin@hackathon.qd2rc.mongodb.net/bank?retryWrites=true&w=majority&authSource=admin'

mongo = PyMongo(app)

users = mongo.db.users
loans = mongo.db.loans

# Operations for users
@app.route('/')
def index():
    return render_template('index.html', users=users.find())

@app.route('/add_user', methods=['POST'])
def add_user():
    '''Registers/creates a new user'''
    new_user = request.form.get('new-user')
    users.insert_one({'text' : new_user})
    return redirect(url_for('index'))

@app.route('/find_user', methods=['GET'])
def get_user_by_username(username):
    ''' Returns the user_by username '''
    query = {'username': username}
    user = users.find_one(query)
    return user if user else None

@app.route('/login', methods=['POST'])
def login(username, password):
    ''' A function that takes in a username and password and returns user '''
    query = {'username': username, 'password': password}
    try:
        user = users.find_one(query)
        return user if user else None
    except BaseException:
        print('Unable to login')
        return None


#Operations for Loans


# Operations for Applications
@app.route('/add_application', methods=['POST'])
def add_application_to_user():
    '''Creates a new loan application for the user'''
#TODO attach the application to a specific user. Query to find user based on username, then attach

    new_application = request.form.get('new-application')
    users.application.insert_one({'text' : users.application, 'complete' : False})
    return redirect(url_for('index'))

@app.route('/complete/<oid>') #not sure we need this
def complete(oid, username):
    '''Takes in a user and an application id, updates it to mark complete'''
    user = get_user_by_username(username)
    application = user.applications.find_one({'_id': ObjectId(oid)})
    application['complete'] = True
    # users.applications.save(user.application)
    return redirect(url_for('index'))

@app.route('/delete_completed_application')
def delete_completed():
    '''Deletes all the applications marked complete'''
    users.applications.delete_many({'complete' : True})
    return redirect(url_for('index'))

# not sure it is needed
# @app.route('/delete_all')
# def delete_all():
#     todos.delete_many({})
#     return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()