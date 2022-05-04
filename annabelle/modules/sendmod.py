import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HANDLER
from annabelle.modules.helpmenu.help_menu import modules_help


@Client.on_message(filters.command(["sendmod", "sm"], prefixes=f"{HANDLER}") & filters.me)
async def sendmod(client: Client, message: Message):
    module_name = message.command[1]
    try:
        await message.edit("<code>Dispatch...</code>")
        text = f"<b>Help for <i>{module_name}</i>\n\nUsage:</b>\n"
        found = False
        for mh in modules_help:
            if list(mh.keys())[0].lower() == module_name.lower():
                found = True
                cmds = list(mh.values()).pop(0)
                for u_cmd in cmds:
                    cmd = list(u_cmd.items())[0]
                    text += f"""<code>{HNDLR + cmd[0]}</code> - <i>{cmd[1]}</i>\n"""
        if not found:
            text = "<b>Module <i>{module_name}</i> not found!</b>"

        if os.path.isfile(f"Mister_Dark_Prince/{module_name.lower()}.py"):
            await client.send_document(
                message.chat.id,
                f"Mister_Dark_Prince/{module_name.lower()}.py",
                caption=text,
            )
        elif os.path.isfile(
            f"Mister_Dark_Prince/custom_modules/{module_name.lower()}.py"
        ):
            await client.send_document(
                message.chat.id,
                f"Mister_Dark_Prince/custom_modules/{module_name.lower()}.py",
                caption=text,
            )
        await message.delete()
    except:
        await message.edit("<b>Invalid module name!</b>")
        await asyncio.sleep(5)
        await message.delete()


modules_help.append(
    {
        "sendmod": [
            {"sendmod [module name]*": "Send one of the modules to the interlocutor"}
        ]
    }
)
