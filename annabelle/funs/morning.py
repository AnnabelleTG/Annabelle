from annabelle import Annabelle
from config import MY_ID
from pyrogram import filters as vrn
from annabelle.helper_funcs.strings import MORNING_TXT

@Annabelle.on_message(vrn.command('morning', HANDLER))
async def morning(Annabelle, message):
      if message.from_user.id == MY_ID:
          message.edit(MORNING_TXT)
