from pyrogram import filters as vrn
from bot import mainbot
from config import HANDLER, MY_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import logging

@mainbot.on_message(vrn.command('start', HANDLER) & vrn.private)
async def start(mainbot, message):
  await message.reply_photo(
    photo = {},
    caption = f"Heya {message.from_user}, I am the horrifying Annabelle userbot made for [this person](t.me/user?id={MY_ID}). The messages you send here will be forwarded to my master",
    reply_markup = InlineKeyboardMarkup([
      [InlineKeyboardMarkup("Deploy your own bot", url="https://github.com/AnnabelleTG/Annabelle")],
      [InlineKeyboardButton("Support Channel", url="t.me/annabelleUB"), InlineKeyboardButton("Group", url="https://t.me/AnnaBelleSupportChat")]
      ])
  )
    
@mainbot.on_message(vrn.incoming & vrn.private)
async def frwd(mainbot, message):
  try:
    USER_ID = message.from_user.mention
    await mainbot.forward_message(message.from_user.id, MY_ID)
  except:
    mainbot.send_message(MY_ID, f"{USER_ID} is spamming me! I am not able to forward his messages")
    
