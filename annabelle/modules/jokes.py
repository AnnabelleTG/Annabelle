import os
import json
import requests
from pyrogram import filters as vrn
from config import HANDLER
from annabelle import Annabelle

API = "https://v2.jokeapi.dev/joke/Any?type=single"

@Annabelle.on_message(filters.command("joke", HANDLER))
async def joke(Annabelle, message):
    request = requests.get(API)
    result = request.json()
    joke = result['joke']
    my_joke = f"""
• **Joke** :\n \n `{joke}`\n.."""
    await message.edit(
        text=my_joke,
        disable_web_page_preview=True,
        quote=True
    )
