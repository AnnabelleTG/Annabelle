from config import HANDLER
from annabelle import Annabelle 

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import ChatAdminRequired, RightForbidden, RPCError

@Annabelle.on_message(filters.command('pin', HANDLER) & filters.group)
async def pin(client: Annabelle, message: Message):
    admins = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not ((admins.status == "administrator") or (admins.status == "creator")):
        await message.reply_text("**Your not allowed to use this.**")
        return
    if not message.reply_to_message:
        await message.reply_text("**Reply to a message to pin.**")
        return
    try:
        message.reply_to_message.pin()
        await message.edit("<code>Pinned successfully!</code>")
    except ChatAdminRequired:
        await message.reply_text("I am not admin here.")
    expect RightForbidden:
        await message.reply_text("I don't have enough rights to pin messages.")
    expect RPCError as error:
        await message.reply_text(f"Some error occurred\n\n*Error:*\n{error}")
        
@Annabelle.on_message(filters.command('unpin', HANDLER))
async def unpin(client: Annabelle, message: Message):
    if not ((admins.status == "administrator") or (admins.status == "creator")):
        await message.reply_text("**Your not allowed to use this.**")
        return
    if not message.reply_to_message:
        await message.reply_text("**Reply to a message to pin.**")
        return
     try:
        message.reply_to_message.pin()
        await message.edit("<code>Unpinned successfully!</code>")
     except ChatAdminRequired:
         await message.reply_text("I am not admin here.")
     expect RightForbidden:
         await message.reply_text("I don't have enough rights to unpin messages.")
     expect RPCError as error:
         await message.reply_text(f"Some error occurred\n\n*Error:*\n{error}")
