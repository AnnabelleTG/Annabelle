from pyrogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  InlineQueryResultArticle,
  InputMessageContent
)
from bot import mainbot

@mainbot.on_callback_query(filters.regex("tools"))
async def calltools(query, message):
  await query.message.edit(
    text = "**TOOLS**\n Here are the plugins available in tools category",
    reply_markup = InlineKeyboardMarkup([
      [InlineKeyboardButton("Thumbnail", callback_data="ytthumb"), InlineKeyboardButton("Github search", callback_data="gitsearch")],
      [InlineKeyboardButton("YT Search", callback_data="ytsearch"), InlineKeyboardButton("Purge", callback_data="callpurge")],
      [InlineKeyboardButton("Create", callback_data="callcreate"), InlineKeyboardButton("Auto pic", callback_data="callautodp")],
      [InlineKeyboardButton("Auto bio", callback_data="callautobio"), InlineKeyboardButton("Covid", callback_data="callcovid")]
    ])
  )

@mainbot.on_inline_query()
async def inline_query(bot:mainbot, iq:InlineQuery):
  result[]
  if iq.query == "pm":
    result.append(
      InlineQueryResultArticle(
        title="dont pm me",
        input_message_content=InputMessageContent("https://www.google.com"),
        reply_markup=InlineKeyboardMarkup([
          [InlineKeyboardButton("test", url="t.me/annabelleub")]
        ])
      ))
    await iq.answer(results=result, cache_time=300)
