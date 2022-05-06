# https://github.com/vaishnavofficial/Annabelle
from annabelle import Annabelle 
from pyrogram import filters as vrn
from config import HANDLER

@Annabelle.on_message(vrn.command('block', HANDLER)) 
async def block(bot, message):
       if message.from_user.id == MY_ID:
         if message.reply_to_message:
           ban_id = message.reply_to_message.from_user.id
           await bot.block_user(ban_id)
           await message.edit("`Haa! Blocked that user`")
         else:
           args = message.text.split(None, 1)
           ban_name = args[1]
           await bot.block_user(ban_name)
           await message.edit("Blocked that user")

@Annabelle.on_message(vrn.command('unblock', HANDLER))
async def unblock(bot, message):
    try:
      if message.from_user.id == MY_ID:
         if message.reply_to_message:
           ban_id = message.reply_to_message.from_user.id
           await bot.unblock_user(ban_id)
           await message.edit("`Haa! Unblocked that user`")
         else:
           args = message.text.split(None, 1)
           ban_name = args[1]
           await bot.unblock_user(ban_name)
           await message.edit("Unblocked that user")
    except Exception as e:
         await message.edit("Something went wrong! Check app logs")
         print(e)
