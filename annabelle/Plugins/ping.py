from time import time
from time import sleep
from pyrogram import filters as vrn
from annabelle.__main__ import Annabelle
from pyrogram.types.messages_and_media import Message


@Annabelle.on_message(vrn.command("ping","?") & vrn.group)
async def ping(bot:Annabelle,msg:Message):
    start = time()
    await msg.edit_text(text="**Ping ...")
    stop = time()
    delay_time = ( stop - start ) * 1000
    ms = str(delay_time).split(".")[0]
    sleep(1) #can be removed
    await edit_text(text=f"""**Pong !!**
**__$__**  `{ms}`  **__ms__**""")

