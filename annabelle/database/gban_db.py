import pymongo
from pymongo import MongoClient

from config import DATABASE_NAME, DATABASE_URL
from annabelle.database.gmutes_db import  check_gmute, un_gmute

client = MongoClient(DATABASE_URL)
mydb = client[DATABASE_NAME]
gban_col = mydb['GBANS']

gmute_check = check_gmute()
def add_gban(id, gmute_check, reason):
  if gmute_check is True:
    un_gmute()
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
  
def chek_gban(id):
  x = gban_col.find_one(id)
  if x:
    return True
  else:
    return False
  
