import asyncio

from config import HANDLER
from annabelle.modules.helpmenu.help_menu import modules_help

from pyrogram.types import Message
from pyrogram import Client, filters

@Client.on_message(filters.command("del", HANDLER) & filters.me)
async def del_msg(client: Client, message: Message):
    if not message.reply_to_message:
        await message.reply_text("Reply to message to delete")
        return
    message_id = message.reply_to_message.message_id
    await message.delete()
    await client.delete_messages(
        chat_id=message.chat.id,
        message_ids=message_id,
    )
    k = await message.reply("I've deleted the message for you")
    await asyncio.sleep(3)
    await k.delete()

@Client.on_message(filters.command("purge", HANDLER) & filters.me)
async def purge(client: Client, message: Message):
    messages_to_purge = []
    if not message.reply_to_message:
        await message.reply_text("Reply to message to purge")
        return
    async for msg in client.iter_history(
        chat_id=message.chat.id,
        offset_id=message.reply_to_message.message_id,
        reverse=True,
        ):
        messages_to_purge.append(msg.message_id)
    for msgs in [
        messages_to_purge[i : i + 1000] for i in range(0, len(messages_to_purge), 1000)
    ]:
        await client.delete_messages(message.chat.id, msgs)
        await asyncio.sleep(1)
        await message.reply("Purge completed")
        await asyncio.sleep(2)
        await message.delete()


modules_help.append(
    {
        "purge": [
            {
                "purge [reply]*": "Reply to a message after which you want to delete messages"
            },
            {"del [reply]*": "Reply to the message you want to delete"},
        ]
    }
)
