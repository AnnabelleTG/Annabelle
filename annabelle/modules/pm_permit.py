from pyrogram import filters as vrn
from userbot import Annabelle
from config import HANDLER
from Annabelle.annabelle.database.pmpermit_db import add_permit, check_permit, del_permit

@Annabelle.on_message(vrn.command('permit', HANDLER) & vrn.outgoing)
async def pmok(Annabelle, message):
   if message.reply_to_message:
      id = message.reply_to_message.from_user.id
      x = check_permit(id)
      if x is True:
         await message.edit("`That person already has the permission to pm you`")
      else:
         add_permit(id)
         await message.edit(f"`{message.reply_to_message.from_user.mention} can pm you from now`")
   else:
      await message.edit("`Don't be a fool! Reply to the user's message`")

@Annabelle.on_message(vrn.command('unpermit', HANDLER) & vrn.outgoing)
async def pmnotok(Annabelle, message):
   if message.reply_to_message:
      id = message.reply_to_message.from_user.id
      x = check_permit(id)
      if x is True:
        del_permit(id)
        await message.edit("`Now that fool can't pm you!")
      else:
        await message.edit("`He was not at all permitted`")
   else:
     await message.edit("`Reply to a message mahn!`")

@Annabelle.on_message(vrn.incoming & vrn.private)
async def vaadamwone(Annabelle, message):
   id = message.from_user.id
   x = check_permit(id)
   if x is True:
      return
   else:
     await message.reply("Don't pm my master. Now wait till he comes and unblocks you")
     await Annabelle.block_user(id)
