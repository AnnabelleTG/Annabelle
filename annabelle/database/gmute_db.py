import pymongo
from pymongo import MongoClient

from config import DATABASE_URL as DB_URL
from config import DATABASE_NAME as DB_NAME

import logging
logging = logging.getLogger(__name__)

mydb = MongoClient(DB_NAME)
gmute_col = mydb['GMUTE']

def add_gmute(id, reason):
  x = gmute_col.find_one(id)
  if x:
    return
  else:
    return gmute_col.insert_one({'_id" : id, 'reason' : reason})
                                 
def check_gmute(id):
   x = gmute_col.find_one(id)
   if x:
     return True, reason
   else:
     return False
                                 
def ungmute(id):
   x = gban_col.find_one(id)
   if x:
      return gban_col.delete_one({'_id : id})
   else:
      return False
