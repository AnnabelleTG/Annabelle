from annabelle import Annabelle
from pyrogram import filters as vrn
from annabelle.helper_funcs.strings import WORK_TXT

async def work(Annabelle, message):
     try:
       if message.from_user.id == MY_ID:
           await message.edit(WORK_TXT)
       else:
           return
     except Exception as e:
        message.edit(f'{e}')
       
