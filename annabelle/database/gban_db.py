import pymongo
from pymongo import MongoClient

from config import DATABASE_NAME, DATABASE_URL
from annabelle.database.gmutes_db import  check_gmute, un_gmute

client = MongoClient(DATABASE_URL)
mydb = client[DATABASE_NAME]
gban_col = mydb['GBANS']

def add_gban(id):
  checks = check_gmute(id)
  if checks is True:
    un_gmute(id)
    x = gban_col.find_one(id)
    if x:
      return 
    else:
      return gban_col.insert_one({'_id' : id, 'reason' : reason})
    
def un_gban(id):
  x = gban_col.find_one(id)
  if x:
    return gban_col.delete_one(id)
  else:
    return False
  
def check_gban(id):
  x = gban_col.find_one(id)
  if x:
    return reason
  else:
    return False
  
