import pytz
import asyncio
import datetime
from ..userbot import Annabelle
from pyrogram import filters as vrn
from config import MY_ID, HANDLER
from pyrogram.types.messages_and_media import Message



@Annabelle.on_message(vrn.command("autobio", HANDLER))
async def autobio(bot:Annabelle, msg:Message) :
    value = msg.text.split(None, 1)
    args = value[1].lower()
    if args == "true" :
        await msg.edit_text(text="**__Plugin Enabled__** : `autobio`")
        while value is "true" :
            await asyncio.sleep(60)
            hour = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).hour
            minute = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).minute
            await bot.update_profile(bio=f"H : {hour} , M : {minute}")

    elif args == "false" :
        await msg.edit_text(text="**__Plugin Disabled__** : `autobio`")

    else :
        await msg.edit_text(text="**__Please input a boolean as a parameter !!__**")
