from userbot import Annabelle
from config import MY_ID, HANDLER
from pyrogram import filters as vrn
from pyrogram.types.messages_and_media import Message



@Annabelle.on_message(filters.command("clone", HANDLER) & filters.me)
async def clone(bot:Annabelle, msg:Message) :
    if msg.from_user.id == MY_ID :
        if msg.chat.type == "group" or msg.chat.type == "supergroup" :
            try :
                user = msg.reply_to_message.from_user

                try :
                    pic = await bot.download_media(message=user.photo.big_file_id)
                    await bot.set_profile_photo(photo=pic)
                except :
                    print("No profile photo !")

                firstname = user.first_name

                if user.last_name :
                    lastname = user.last_name
                else :
                    lastname = ""

                await bot.update_profile(first_name=firstname, last_name=lastname)
                await msg.edit_text(text="`Cloned Successfully !`")

            except :
                await msg.edit_text(text="`Couldnt clone !!`")


        elif msg.chat.type == "private" :
            try :

                try :
                    user = msg.chat
                except :
                    user = msg.reply_to_message.from_user

                try :
                    pic = user.photo.big_file_id
                    await bot.set_profile_photo(photo=pic)
                except :
                    pic = ""

                firstname = user.first_name
                
                if user.last_name :
                    lastname = user.last_name
                else :
                    lastname = ""

                await bot.update_profile(first_name=firstname, last_name=lastname)

                await msg.edit_text(text="`Cloned Successfully !`")
            except :
                await msg.edit_text(text="**Couldnt Clone ! :( `")
        else :
            await msg.edit_text(text="`Couldnt Clone !`")

