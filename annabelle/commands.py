from pyrogram import Client, filters

from config import BOT_TOKEN, API_ID, API_HASH, HANDLER

Annabelle = Client(
        api_id = API_ID,
        api_hash = API_HASH
        bot_token = BOT_TOKEN,
        session_name = SESSION_STRING
      )

@Annabelle.on_message(filters.command('repo', HANDLER))
async def repo(Client, message):
     
