from pyrogram import Client, filters
from pyrogram.types import Message
from config import HANDLER
from annabelle.modules.helpmenu.help_menu import modules_help


@Client.on_message(filters.command(["block"], prefixes=f"{HANDLER}") & filters.me)
async def block_True(client: Client, message: Message):
    try:
        user_id = message.command[1]
        await client.block_user(user_id)
        await message.edit(
            f"<b>😡 The <a href='tg://user?id={user_id}'>user</a> is now blacklisted!</b>"
        )
    except Exception as e:
        await message.edit(f"<b>😨 Ooops:</b> <code>{e}</code>")


@Client.on_message(filters.command(["unblock"], prefixes=f"{HANDLER}") & filters.me)
async def unblock(client: Client, message: Message):
    try:
        user_id = message.command[1]
        await client.unblock_user(user_id)
        await message.edit(
            f"<b>☺️ <a href='tg://user?id={user_id}'>User</a> removed from the blacklist!</b>"
        )
    except Exception as e:
        await message.edit(f"<b>😰 Oops:</b> <code>{e}</code>")


modules_help.append(
    {
        "blacklist": [
            {"block [user_id]*": "Block user"},
            {"unblock [user_id]*": "Unblock user"},
        ]
    }
)
