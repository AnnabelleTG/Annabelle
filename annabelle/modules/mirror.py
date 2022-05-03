from pyrogram import Client, filters
from pyrogram.types import Message
from config import HANDLER
from annabelle.modules.helpmenu.help_menu import modules_help
from annabelle.modules.helpers.mirror_func import make

@Client.on_message(
    filters.command(["ll", "rr", "dd", "uu"], prefixes=f"{HANDLER}") & filters.me
)
async def mirror_flip(client: Client, message: Message):
    await message.edit("<code>Processing...</code>")
    param = {"ll": 1, "rr": 2, "dd": 3, "uu": 4}[message.command[0]]
    await make(client, message, param)


modules_help.append(
    {
        "mirror_flip": [
            {"ll [reply on photo or sticker]*": "reflects the left side"},
            {"rr [reply on photo or sticker]*": "reflects the right side"},
            {"uu [reply on photo or sticker]*": "reflects the top"},
            {"dd [reply on photo or sticker]*": "reflects the bottom"},
        ]
    }
)
