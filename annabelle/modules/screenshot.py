import asyncio
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from config import HANDLER
from annabelle.modules.helpmenu.help_menu import modules_help

@Client.on_message(
	filters.command(["scr", "screenshot"], prefixes=f"{HANDLER}") & filters.me
	)
async def scrshot(client: Client, message: Message):
	quantity = int(message.command[1])
	chat = message.chat.id
	await message.delete()
	for _ in range(quantity):
		await asyncio.sleep(2)
		await client.send(
			functions.messages.SendScreenshotNotification(
				peer = await client.resolve_peer(chat),
				reply_to_msg_id = 0,
				random_id = rnd_id(),
				)
			)


modules_help.append(
    {
        "screenshot": [
            {
                "scr [amount of screenshots]": "Take a screenshot\nThis only works in private messages!"
            }
        ]
    }
)
