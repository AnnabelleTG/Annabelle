from pyrogram.types import (
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  InlineQueryResultArticle,
  InputMessageContent
)
from bot import mainbot

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
