import os
import pymongo

from bank.user import User, ApplicationInfo

# connecting to the cluster using Mongoclient
try:
    db = pymongo.MongoClient(os.getenv('MONGO_URI2')).bank
    # put env variable export MONGO_URI="mongodb+srv://admin:admin@hackathon.qd2rc.mongodb.net/bank?retryWrites=true&w=majority&authSource=admin").bank
    print("Connected to Mongodb database successfully.")
except:
    print("Did not connect to the database")
    raise

_users = db.users

# CRUD operations on user.
def create_user(new_user: User):
    ''' Creates a new user in the database '''
    try:
        _users.insert_one(User.to_dict())
        print('User created')
    except Exception:
        print('Unable to create user')

# 2. Get user by query
def get_all_users():
    ''' Returns all users '''
    return list(_users.find({}))

def login(username, password):
    ''' A function that takes in a username and password and returns user object '''
    query_dict = {'username': username, 'password': password}
    try:
        user_dict = _users.find_one(query_dict)
        return User.from_dict(user_dict) if user_dict else None
    except BaseException:
        print('Unable to login')
        return None

def get_user_by_username(username):
    ''' Returns the user_by username '''
    query = {'username': username}
    user = _users.find_one(query)
    return User.from_dict(user) if user else None

def get_users_by_income(income):
    ''' Returns the user_by username '''
    query = {'income': income} # TODO make this take in a range
    return list(_users.find(query))



# 3. Update user
# update_user = db.users.update_one({"username":"sandraroy"},
#                             {"$set": { "address":"Manhattan, NY"}
#                             })

# 4. delete user
def remove_user_by_username(username):
    ''' A function that takes in a username and deletes user from the  '''
    query = {'username': username}
    try:
        _users.delete_one(query)
        print('User {username} deleted')
    except BaseException:
        print('Unable to delete')
        return None