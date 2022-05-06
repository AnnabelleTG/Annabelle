from annabelle import Annabelle 
from pyrogram import filters as vrn

@Annabelle.on_message(filters.command('pin', '?') & filters.group)
async def pin(Annabelle, message):
    if not admins:
        return
    else:
      try:
        message_id = message.reply_to_message.message_id
        await bot.pin_chat_message(message.chat.id, message_id)
        await message.edit("<code>Pinned successfully!</code>")
      except:
        await message.edit("Reply to the message you want to pin")

@Annabelle.on_message(vrn.command('unpin', '?'))
async def unpin(Annabelle, message):
    if not admins:
        return
    else:
     try:
        message_id = message.reply_to_message.message_id
        await bot.unpin_chat_message(message.chat.id, message_id)
        await message.edit("<code>Unpinned successfully!</code>")
     except:
        await message.edit("Reply to the message you want to unpin")
