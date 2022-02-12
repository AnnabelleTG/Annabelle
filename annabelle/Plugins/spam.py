import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from annabelle.helper_funcs.PyroHelp import ReplyCheck


@Client.on_message(filters.command("spam", ".") & filters.me)
async def spam(bot, _, message: Message):
    await message.delete()

    times = message.command[1]
    to_spam = " ".join(message.command[2:])

    if message.chat.type in ["supergroup", "group"]:
        for _ in range(int(times)):
            await bot.send_message(
                message.chat.id, to_spam, reply_to_message_id=ReplyCheck(message)
            )
            await asyncio.sleep(0.20)

    if message.chat.type == "private":
        for _ in range(int(times)):
            await bot.send_message(message.chat.id, to_spam)
            await asyncio.sleep(0.20)



