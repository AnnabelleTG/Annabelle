import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from config import HANDLER
from annabelle.modules.helpmenu.help_menu import modules_help


@Client.on_message(filters.command(["fwdall"], prefixes=f"{HNDLR}") & filters.me)
async def forward(client: Client, message: Message):
    stat = None if len(message.text.split(" ")) < 2 else message.text.split(" ")[1]
    if sta is not None:
        await message.edit("<code>On it...</code>", parse_mode="html")
        try:
            target = await client.get_chat(stat)
        except:
            await message.edit("<code>Unknown target.</code>", parse_mode="html")
            target = None
        if target is not None:
            msgs = []
            async for msg in client.iter_history(message.chat.id, reverse=True):
                msgs.append(msg.message_id)
                if len(msgs) >= 100:
                    try:
                        await client.forward_messages(target.id, message.chat.id, msgs)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                        await client.forward_messages(target.id, message.chat.id, msgs)
                    msgs = []
            if msgs:
                try:
                    await client.forward_messages(target.id, message.chat.id, msgs)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    await client.forward_messages(target.id, message.chat.id, msgs)
            await message.edit("<code>Forwarded successfully.</code>", parse_mode="html")
    else:
        await message.edit("<code>No target passed.</code>", parse_mode="html")


modules_help.append(
    {
        "forwardall": [
            {
                "fwdall [target]*": "Foraward all messages to defined target [username/chat_id/chat_link]."
            }
        ]
    }
)
