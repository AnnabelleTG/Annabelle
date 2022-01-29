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
          message.edit(GBAN_TXT.format(message.reply_to_message.from_user.mention, None if reason is None else reason))
