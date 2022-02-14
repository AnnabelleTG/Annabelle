import json
from pyrogram import Client
from userbot import Annabelle
from pyrogram import filters as vrn
from youtubesearchpython import SearchVideos
from pyrogram.types.messages_and_media import Message



@Annabelle.on_message(vrn.command("yt", HANDLER))
async def yt(bot:Client, msg:Message) :
    if msg.from_user.id == MY_ID :
        try :
            query = msg.text.replace("?yt", "")
            await msg.edit_text(text=f"""**__getting Youtube Video ...__**

**Search_Query** : `{query}`""")
            search = SearchVideos(query, mode="json", max_results=1)
            raw_out = search.result()
            json_data = json.loads(raw_out)
            filter1 = json_data["search_result"]
            filter2 = filter1[0]
            link = filter2["link"]
            await msg.edit_text(text=f"""**__Search Result__**

**Query **: `{query}`
**Link **: {link}""")
        except :
            await msg.edit_text(text="**Couldnt Fetch video !")
