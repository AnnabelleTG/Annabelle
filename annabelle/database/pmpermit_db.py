import pymongo
from pymongo import MongoClient
from config import (
  DATABASE_NAME,
  DATABASE_URL
)

client = MongoClient(DATABASE_URL)
mydb = client[DATABASE_NAME]
pm_col = mydb['PM PERMITS']

def add_permit(id):
  x = pm_col.find_one(id) # to avoid duplicate ids
  if x:
    return False
  else:
    return pm_col.insert_one({'_id' : id})
  
def check_permit(id):
  x = pm_col.find_one(id)
  if x:
    return True
  else:
    return False
  
def del_permit(id):
  x = check_permit(id)
  if x is True:
    return pm_col.delete_one({'_id' : id})
  else:
    return False
