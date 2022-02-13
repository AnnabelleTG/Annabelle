import time
from config import HANDLER
from pyrogram import filters as vrn
from ...userbot import Annabelle
from pyrogram.types.messages_and_media import Message


@Annabelle.on_message(vrn.command("ping", HANDLER) & vrn.group)
async def ping(bot:Annabelle,msg:Message):
    start = time.time()
    await msg.edit_text(text="**Ping ...")
    stop = time.time()
    delay_time = ( stop - start ) * 1000
    ms = str(delay_time).split(".")[0]
    time.sleep(1) #can be removed
    await msg.edit_text(text=f"""**Pong !!**
**__$__**  `{ms}`  **__ms__**""")
