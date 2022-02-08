from asyncio import sleep
from config import MY_ID, HANDLER, AUTODP_DUMP
from annabelle import Annabelle
from pyrogram import filters as vrn

import logging
logging = looging.getLogger(__name__)

@Annabelle.on_message(vrn.command('autopic', HANDLER))
async def autopic(Annabelle, message):
  if message.from_user.id == MY_ID:
    args = message.text.split(None, 1)
    if len(args) >= 2:
      toggle = args[1]
      if toggle.lower() in ["on", "yes", "true"]:
        AUTODP = True
      elif toggle.lower() in ["off", "no", "false"]:
        AUTODP = False
      else:
        await message.edit("Sorry, I couldn't understant whether you told to on or off")
        
  else:
      await message.edit("`Command incomplete`")
      
while AUTODP is True:
   async for pro in Annabelle.get_message(AUTODP_DUMP):
     if pro.type == "photo":
        await Annabelle.set_profile_photo(photo=pro)
     else:
        countinue
   
