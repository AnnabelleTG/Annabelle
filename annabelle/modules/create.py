from annabelle import Annabelle 
from pyrogram import filters as vrn

@Annabelle.on_message(vrn.command('group', HANDLER))
async def create_gr(Annabelle, message):
       if message.from_user.id == MY_ID:
         if message.reply_to_message:
           try:
             add_id = message.reply_to_message.from_user.id
             args = message.text.split(None, 1)
             title = args[1]
             await Annabelle.create_group(title, add_id)
             await message.edit(f"`successfully made a new group {title}`")
           except:
             await message.edit("`That user cant be added to a group`")

@Annabelle.on_message(vrn.command('channel', HANDLER))
async def create_ch(Annabelle, message):
       if message.from_user.id == MY_ID:
         args = message.text.split(None, 1)
         title = args[1]
         await Annabelle.create_channel(title, 'made with annabelle userbot')
         await message.edit(f"`successfully made a new channel {title}`")
