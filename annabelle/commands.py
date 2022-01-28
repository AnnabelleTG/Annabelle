from pyrogram import Client
from pyrogram import filters as vrn

from config import BOT_TOKEN, API_ID, API_HASH, HANDLER

from annabelle.funs.work import work

Annabelle = Client(
        api_id = API_ID,
        api_hash = API_HASH
        bot_token = BOT_TOKEN,
        session_name = SESSION_STRING
      )

@Annabelle.on_message(vrn.command('repo', HANDLER))
async def repo(Client, message):
     message.edit("Hey, I am using Annabelle userbot"
                  "Its easy and powerful. Deploy your own now"
                  "https://github.com/Vaishnavofficial/Annabelle")

@Annabelle.on_message(vrn.command('work', HANDLER))
async def prwork(Annabelle, message):
      work()
