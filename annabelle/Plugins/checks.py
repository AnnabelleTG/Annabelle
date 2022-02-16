from userbot import Annabelle
from annabelle.database.gbans import check_gban
from annabelle.database.gmutes import check_gmute
from config import MY_ID
from pyrogram.types import ChatPermissions

@Annabelle.on_message(filters.new_chat_member & filters.group)
async def ayoo(Annabelle, message):
  id = message.from_user.id
  member = await Annabelle.get_chat_member(message.chat.id, MY_ID)
  x = check_gban(id)
  if x is not False:
    try:
      await bot.kick_chat_member(message.chat.id, id)
      await message.reply(f"`Recently joined user is globally banned! I have kicked him`\nreason:`{x}`")
    except:
      await message.reply(f"`Warning! Recently joined user is globally banned!`\nreason: `{x}`")
  else:
    id = message.from_user.id
    x = check_gmute(id)
    if x is not False:
      try:
        await Annabelle.restrict_chat_member(message.chat.id, id, ChatPermissions())
        await message.reply(f"`Recently joined user is globally muted!` I have muted him`\nreason: `{x}`")
      except:
        await message.reply(f"`WARNING\n Recently joined user is globally muted for reason: {x}`")
        
        
        # hope it works
