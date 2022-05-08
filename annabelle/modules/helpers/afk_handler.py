# functions

import datetime
from pyrogram import Client, filters

async def afk_handler(client, message):
    try:
        global start, end, reason
        end = datetime.datetime.now().replace(microsecond=0)
        afk_dur = end - start
        user_is_bot = message.from_user.is_bot
        if user_is_bot is False:
            await message.reply_text(
                f"<b>I afk {afk_dur}</b>\n" f"<b>Reason:</b> <i>{reason}</i>"
            )
    except NameError:
        pass
