from config import HANDLER
from pyrogram import filters
from annabelle import Annabelle 
from pyrogram.types import Message

@Annabelle.on_message(filters.command('pin', HANDLER) & filters.group)
async def pin(client: Annabelle, message: Message):
    admins = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not ((admins.status == "administrator") or (admins.status == "creator")):
        await message.reply_text("**Your not allowed to use this.**")
        return
    try:
        message_id = message.reply_to_message.message_id
        await bot.pin_chat_message(message.chat.id, message_id)
        await message.edit("<code>Pinned successfully!</code>")
    except:
        await message.edit("Reply to the message you want to pin")

@Annabelle.on_message(filters.command('unpin', HANDLER))
async def unpin(client: Annabelle, message: Message):
    if not ((admins.status == "administrator") or (admins.status == "creator")):
        await message.reply_text("**Your not allowed to use this.**")
        return
     try:
        message_id = message.reply_to_message.message_id
        await bot.unpin_chat_message(message.chat.id, message_id)
        await message.edit("<code>Unpinned successfully!</code>")
     except:
        await message.edit("Reply to the message you want to unpin")
