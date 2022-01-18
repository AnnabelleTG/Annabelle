async def create_gr(bot, message):
       if message.from_user.id == MY_ID:
         if message.reply_to_message:
           try:
             add_id = message.reply_to_message.from_user.id
             args = message.text.split(None, 1)
             title = args[1]
             await bot.create_group(title, add_id)
             await message.edit(f"`successfully made a new group {title}`")
           except:
             await message.edit("`That user cant be added to a group`")

async def create_ch(bot, message):
       if message.from_user.id == MY_ID:
         args = message.text.split(None, 1)
         title = args[1]
         await bot.create_channel(title, 'made with annabelle userbot')
         await message.edit(f"`successfully made a new channel {title}`")
