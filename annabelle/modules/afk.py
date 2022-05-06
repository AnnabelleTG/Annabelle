"""


# Copyright Here


"""
import asyncio
import datetime
from pyrogram import Client, filters
from pyrogram.handlers import (
	MessageHandler
	)
from config import HANDLER
from annabelle.modules.helpers.afk_helpers import afk_handler
from annabelle.modules.helpmenu.help_menu import modules_help

@Client.on_message(filters.command("afk", prefixes=f"{HANDLER}") & filters.me)
async def afk(client: Client, message):
	global start, end, handler, reason
	start = datetime.datetime.now().replace(microsecond=0)
	handler = await client.add_handler(
		MessageHandler(afk_handler, (filters.private & ~filters.me))
		)
		if len(message.command) >= 1:
                        reason = message.text.split(" ", maxsplit=1)[1]
                        await message.edit(f"I'm going afk\n**reason**: `{reason}`")
		else:
			reason = None
            await message.edit("I'm going afk")
            
            
@Client.on_message(filters.command("unafk", prefixes=f"{HANDLER}") & filters.me)
async def unafk(client: Client, message):
	try:
	    global start, end
            end = datetime.datetime.now().replace(microsecond=0)
            afk_dur = end - start
            await message.edit(f"I'm not AFK any more. I was AFK {afk_dur}")
            client.remove_handler(*handler)
      except NameError:
      	await message.edit("You aren't AFK Now")
      	await asyncio.sleep(3)
      	await message.delete()
      	
modules_help.append(
    {"afk": [{"afk [reason]": "Go to afk"}, {"unafk": "Get out of AFK"}]}
)    
