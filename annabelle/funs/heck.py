from pyrogram import filters as vrn
from userbot import Annabelle
from config import HANDLER

import asyncio
from asyncio import sleep

import logging
logging = logging.getLogger(__name__)

@Annabelle.on_message(vrn.command('hack', HANDLER) & vrn.outgoing)
def hack(Annabelle, message):
  if message.reply_to_message:
    message.edt("`hacking.....`")
    asyncio.sleep(1)
    message.edit("`getting chats`")
    asyncio.sleep(2)
    message.edit("`got all chats`")
    asyncio.sleep(1)
    message.edit("`cracking user password`")
    asyncio.sleep(1)
    message.edit(f"`hacking finished. Pay $80 to {message.from_user.mention} to attain back your info`")
