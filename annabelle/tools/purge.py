from config import HANDLER
from pyrogram import Client
from pyrogram import filters as vrn
from userbot import Annabelle
from pyrogram.types.messages_and_media import Message


async def purge(bot:Client, msg:Message):
    chat_id = msg.chat.id
    user_id = msg.from_user.id
    try :
        start = msg.reply_to_message.message_id
        admin = bot.get_chat_member(chat_id, user_id=user_id)
        admin_type = ("adminsistrator", "creator")
        count = 0
        if admin.status == admin_type :
            await bot.send_message(chat_id, text="**Starting to delete messages !!**")
            for message in await bot.get_history(chat_id, offset_id=start, reverse=True) :
                msg_id = message.message_id
                await bot.delete_messages(chat_id, msg_id)
                count += 1
            await bot.send_message(chat_id, text=f"""**Deleted !!**
**Count : ** `{count - 1}` """)
        else :
            await msg.edit_text(text="**Seems you are not an admin of the group**")

    except :
        await msg.edit_text(text="**__Offset not specified !!__**")

