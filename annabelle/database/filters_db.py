import pymongo
from pymongo import MongoClient

from annabelle import DATABASE_NAME, DATABASE_URL

import logging
logging = logging.getLogger(__name__)

client = MongoClient(DATABSE_NAME)
mydb = client[DATABASE_NAME]
filter_col = mydb['FILTERS']

def add_filter(keyword, reply, type):
  x = check_filter()
  if x is True:
    rm_filter(keyword)
    return filter_col.insert_one({'_id' : keyword, 'reply' : reply, 'type' : type})
  else:
    return False
    
def check_filter(keyword, type, reply):
  x = filter_col.find_one({'_id' : keyword})
  if x:
    return True, keyword, type, reply
  else:
    return False
  
def rm_filter(keyword):
  x = check_filter()
  if x:
    return filter_col.delete_one(keyword)
  else:
    return False
  
def replace_filter(keyword, reply):
  x = check_filter()
  if x is True:
    filter_col.update_one({'_id' : keyword, 'reply' : reply})
