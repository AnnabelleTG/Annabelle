import wikipedia
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HANDLER
from annabelle.modules.helpmenu.help_menu import modules_help

@Client.on_message(filters.command("wiki", prefixes=f"{HANDLER}") & filters.me)
async def wiki(client: Client, message: Message):
    lang = message.command[1]
    user_request = " ".join(message.command[2:])
    if user_request == "":
        wikipedia.set_lang("en")
        user_request = " ".join(message.command[1:])
    try:
        if lang == "ml":
            wikipedia.set_lang("ml")

        result = wikipedia.summary(user_request)
        await message.edit(
            f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{result}</code>"""
        )

    except Exception as exc:
        await message.edit(
            f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>"""
        )


modules_help.append(
    {"wikipedia": [{"wiki [lang] [request]*": "Search in Russian Wikipedia"}]}
)

requirements_list.append("wikipedia")
