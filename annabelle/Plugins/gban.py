from config import MY_ID
from annabelle.helper_funcs.admin_check import admin_check
from annabelle.helper_funcs.strings import GBAN_TXT
from annabelle.commands import Annabelle

import logging

G_BANS = dict({})

async def gban(Annabelle, message):
    if message.from_user.id == MY_ID
      if message.reply_to_message:
          if message.reply_to_message.from_user.id not in G_BANS.keys()
             args = message.text.split(None, 1)
             if len(args) >= 2:
                 reason = args[1]
             else:
                 reason = None
          G_BANS[message.reply_to_message.from_user.id] = reason if reason is not None else None
          message.edit(GBAN_TXT.format(message.reply_to_message.from_user.mention, None if reason is None else reason))

@Annabelle.on_message(filters.new_chat_members & filters.group)
async def gban_kodk(Annabelle, message):
     if message.from_user.id in G_BANS.keys():
        member = await client.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if member.can_delete_messages:
           await Annabelle.kick_chat_member()
           await message.edit(r"The recently joined user is globally banned. I have kicked him/her")
        else:
           await message.edit(r"Recently joined user is Globally banned! I can't kick him/her due to lack of permission")
