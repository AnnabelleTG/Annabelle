from annabelle import Annabelle
from pyrogram import filters as vrn

@Annabelle.on_message(vrn.command('setemoji', HANDLER))
async def setemoji(Annabelle, message):
      if message.from_user.id == MY_ID:
          args = message.text.split(None, 1)
          if len(args) >= 2:
             ALIVE_EMOJI = Args[1]
             await message.edit(f"`ALIVE_EMOJI has been set to {ALIVE_EMOJI}")
            
          else:
             await message.edit("`At least mention what to reply with!`")
