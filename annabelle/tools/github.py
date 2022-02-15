import json
import requests
from userbot import Annabelle
from config import MY_ID, HANDLER
from pyrogram import filters as vrn
from pyrogram.types.messages_and_media import Message


@Annabelle.on_message(filters.command("github", HANDLER))
async def github(bot:Annabelle, msg:Message) :
    if msg.from_user.id == MY_ID :
        args = msg.text.split(None, 1)
        if len(args) >= 2:
            query = args[1]
            await msg.edit("`searching github...`")
            try :
              get_url = f"https://api.github.com/search/users?q={query}"
              request1 = requests.get(get_url)
              json_data = request1.json()
              raw_data = json_data["items"]
              data_ = raw_data[0]
              url = data_["url"]
              request2 = requests.get(url)
              data = request2.json()
              await msg.edit_text(text=f"""<p> **__Stdout__**
**Query** : `{query}`

**ID** : `{data["id"]}`
**Url** : <a href="{url}"> ʟɪɴᴋ </a>
**Type** : `{data["type"]}`
**Name** : `{data["name"]}`
**Login** : `{data["login"]}`
**Public Repos** : `{data["public_repos"]}`
**Following** : `{data["following"]}`
**Followers** : `{data["followers"]}`
**Email** : `{data["email"]}`

**ANABELLE USERBOT**
""")
           except :
              await msg.edit_text(text=f"**Couldnt find results for** `{query}`")
        else:
            await message.edit("`Give a username to search`")

