import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


API = "https://api.sumanjay.cf/covid/?country="

@Annabelle.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await message.reply_text(
        text=covid_info(query),
        disable_web_page_preview=True,
        quote=True,
        reply_markup=reply_markup
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""
**♻️ Covid 19 Information**
**🌐 Country :** `{country}`
**🎭 Actived :** `{active}`
**✅ Confirmed :** `{confirmed}`
**⚰️ Deaths :** `{deaths}`
**🆔 ID :** `{info_id}`
**🚨 Last Update :** `{last_update}`
**⚓ Latitude :** `{latitude}`
**🗼 Longitude :** `{longitude}`
**🎙️ Recovered :** `{recovered}`
"""
        return covid_info
    except Exception as error:
        return error


@Annabelle.on_message(filters.command("corona"))
async def covid(Annabelle, message):
    query = message.text.split(None, 1)[1]
    reply_markup = BUTTONS
    await message.reply_text(
        text=covid_info(query),
        disable_web_page_preview=True,
        quote=True
    )
