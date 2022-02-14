# https://github.com/vaishnavoffic
from pyrogram import Client
from config import SESSION_STRING, API_iD , API_HASH

Annabelle = Client( # userbot client  
  api_id = API_ID,
  api_hash = API_HASH,
  bot_token = "xxxxxxx",
  session_name = SESSION_STRING
)


print("Annabelle userbot has started!")
Annabelle.run()
