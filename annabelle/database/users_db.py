import pymongo
from pymongo import MongoClient

from config import (
  DATABASE_NAME,
  DATABASE_URL
)

client = MongoClient(database_url)
mydb = client['USER BOT']
user_col = mydb['USERS']
chat_col = mydb['CHATS']

def add_user(id):
  x = user_col.find_one(id)
  if x:
    return 
  else:
    return user_col.insert_one({'_id' : id})
  
def check_user(id):
  x = user_col.find_one(id)
  if x:
    return True
  else:
    return False
  
  
