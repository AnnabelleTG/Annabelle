from config import MY_ID
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
