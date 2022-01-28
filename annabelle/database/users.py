import motor.motor_asyncio
import logging
import pymongo
   
from config import DATABASE_NAME, DATABASE_URL

logging = logging.getLogger(__name__)

class Database:

      def __init__(self, url, name):
          self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
          self.db = self._client[database_name]
          self.col = self.db.users
          self.grp = self.db.groups

      async def add_user(self, id, name):
          data = {'_id' : id, 'name' : name}
          self.col.insert_one(data)
     
      async def del_user(self, id, name):
          data = {'_id' : id}
          self.col.delete_one(data)
     
      async def find_grp(self, chat, name):
          chat = self.grp.find_one({'id':int(chat)})
          return False if not chat else chat.get('chat_status')

 
