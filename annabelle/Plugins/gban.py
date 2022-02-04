from config import MY_ID, HANDLER
from pyrogram import filters as vrn
from annabelle.helper_funcs.admin_check import admin_check
from annabelle.helper_funcs.strings import GBAN_TXT
from annabelle.commands import Annabelle
from annabelle.database.gban_db import add_gban, un_gban, check_gban

import logging
logging = logging.getLogger(__name__)

@Annabelle.on_message(vrn.command('gban', HANDLER))
async def gban(Annabelle, message):
    if message.from_user.id == MY_ID:
        if message.reply_to_message:
            args = message.text.split(None,1)
            if len(args) >= 2:
                reason = args[1]
                id = message.reply_to_message.from_user.id
                member = Annabelle.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                add_ban(id, reason)
                await message.edit(GBAN_TXT.format(message.reply_to_message.from_user.mention, reason))
            else:
                reason = ""
        else:
            await message.edit("You didn't specify whom to gban")
   else:
     return
                
