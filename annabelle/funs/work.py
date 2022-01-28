from annabelle.commands import Annabelle
from pyrogram import filters as vrn
from annabelle.helper_funcs.strings import WORK_TXT

@bot.on_message(filters.command('work', '?'))
async def work(bot, message):
       if message.from_user.id == MY_ID:
           await message.edit(WORK_TXT)
       else:
           return
