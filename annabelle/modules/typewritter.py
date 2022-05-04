# don't type large text.. Your account will be banned ❗️

import asyncio
import time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from config import HANDLER
from annabelle.modules.helpmenu.help_menu import modules_help

@Client.on_message(filters.command("type", prefixes=f"{HANDLER}") & filters.me)
async def type(client: Client, message: Message):
    orig_text = " ".join(message.command[1:])
    text = orig_text
    tbp = ""
    typing_symbol = "⌨️"

    while tbp != text:
        try:
            await message.edit(tbp + typing_symbol)
            await asyncio.sleep(0.1)

            tbp += text[0]
            text = text[1:]

            await message.edit(tbp)
            await asyncio.sleep(0.1)

        except FloodWait as e:
            time.sleep(e.x)


modules_help.append(
    {
        "type": [
            {
                "type [text]*": "Typing emulation\nDon't use for a lot of characters. Your account may be banned!"
            }
        ]
    }
)
