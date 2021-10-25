import os
from pymongo import MongoClient

# connecting to the cluster using Mongoclient
try: 
    db = MongoClient("mongodb+srv://admin:admin@hackathon.qd2rc.mongodb.net/bank?retryWrites=true&w=majority&authSource=admin").bank
    print("Connected to Mongodb database successfully.")

except:
    print("Did not connect to the database")
    raise


# CRUD operations on user.

# 1. Insert new user
# post = {"name":"Annie Lynnete", "username":"johndanny","password":"johnypass","income":100000,"address":"Chicago, IL","loan_status":""}
# db.users.insert_one(post)

# 2. Get user by name
# user = db.users.find_one({"name":"Erin Tynan"})
# print(user)

# 3. Update user
# update_user = db.users.update_one({"username":"sandraroy"}, 
#                             {"$set": { "address":"Manhattan, NY"}
#                             })

# 4. delete user
# db.users.delete_one({"username":"johndanny"})
