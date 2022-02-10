from pyrogram import filters as vrn
from userbot import Annabelle
from config import MY_ID, HANDLER

@Annabelle.on_message(vrn.command('youtube', HANDLER))
async def youtube(Annabelle, message):
  if message.from_user.id == MY_ID:
    args = message.text.split(None, 1)
    if len(args) >= 2:
      try:
       query = args[1]
       results = Annabelle.get_inline_bot_results("vid", query)
       message.edit("`Searching in youtube...`")
       asyncio.sleep(2)
       message.edit(results)
      except Exception as e:
        message.edit(f"`Can't make a search now`\n{e}")
        print(e)
    else:
      message.edit("`You haven't given a query`")
      
