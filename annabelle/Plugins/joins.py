# https://github.com/AnnabelleTG/annabelle
# This file is made for the above repo. Don't use this without permission

import logging

from userbot import Annabelle
from pyrogram import filters as vrn
from pyrogram.types import ChatPermissions
from annabelle.database.gban_db import chek_gban

@Annabelle.on_message(vrn.new_chat_members)
async def saygban(Annabelle, message):
  x = await Annabelle.get_chat_member(message.chat.id, MY_ID)
  if x.stats in ["administrator", "creator"]:
    try:
      await Annabelle.kick_chat_member(message.chat.id, message.from_user.id)
      await message.edit(f"`The recently joined user is globally banned! I have kicked him")
    except Exception as e:
      await message.edit(f"`Golobaaly banned user. Error while kicking\n\n{e}")
  else:
    await message.edit("`recently joined user is globally banned. I can't kick him due to missing permissions")
