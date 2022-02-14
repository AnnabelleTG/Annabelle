"""
ALL THIS CODE IS WRITTEN FOR ANNEBELLE USER BOT, ANY TYPE OF COPYRIGHT OR KANGING IS STRICTLY PROHIBITED AND MAY LEAD TO COPYRIGHT STRIKE
THIS REPO IS UNDER MIT LICENCE 2022 
CODE BY : [SAMINSUMESH](PAULWALKER_TG)

"""

from pyrogram import Client as Annabelle
from pyrogram import filters
from pyrogram.types import Message
from config import HNADLER

the_regex = r"^r\/([^\s\/])+"

f = filters.chat([])


@Annabelle.on_message(f)
async def auto_read(bot, message: Message):
    await bot.read_history(message.chat.id)
    message.continue_propagation()


@Annabelle.on_message(filters.command("autoscroll", HANDLER) & filters.me)
async def add_to_auto_read(_, message: Message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Autoscroll deactivated")
    else:
        f.add(message.chat.id)
        await message.edit("Autoscroll activated")


# This features helps to scroll to the new messages
