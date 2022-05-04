import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HANDLER
from annabelle.modules.helpmenu.help_menu import modules_help

@Client.on_message(filters.command("tagall", prefixes=f"{HANDLER}") & filters.me)
async def tagall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    string = ""
    limit = 1
    icm = client.iter_chat_members(chat_id)
    async for member in icm:
        tag = member.user.username
        if limit <= 10:
            string += f"@{tag}\n" if tag != None else f"{member.user.mention}\n"
            limit += 1
        else:
            await client.send_message(chat_id, text=string)
            limit = 1
            string = ""
            await asyncio.sleep(2)


modules_help.append({"tagall": [{"tagall": "Tag all members"}]})
