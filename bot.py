from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

mainbot = Client(
  api_id = API_ID,
  api_hash = API_HASH,
  bot_token = BOT_TOKEN,
  session_name = "Annabelle-userbot")


print("Mainbot has started!")
mainbot.run()
