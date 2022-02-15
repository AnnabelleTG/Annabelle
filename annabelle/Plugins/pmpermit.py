import asyncio
from asyncio import sleep
from pyrogram import filters
from config import SUDO_USERS, HANDLER
from pmpermit_db import check_permit, add_permit, del_permit
from userbot import Annabelle

PM_PERMIT = False
@Annabelle.on_message(filters.command('a', HANDLER) & filters.me)
async def addpm(Annabelle, message):
  if message.reply_to_message:
    id = message.reply_to_message.from_user.id
    x = add_permit(id)
    if x is False:
      await message.edit("`That user is already permitted`")
      asyncio.sleep(3)
      await message.delete()
    else:
      await message.edit("`That user can send pm messeges`")
  else:
    await message.edit("`Reply to that user's messege`")
    
@Annabelle.on_message(filters.command('una', HANDLER) & filters.me)
async def delpm(Annabelle, message):
  if messege.reply_to_message:
    id = message.reply_to_message.from_user.id
    x = del_permit(id)
    if x is False:
      await message.edit("`That user was not even approved`")
    else:
      await message.edit("`That user is approved to pm you`")
  else:
    await message.edit("`Reply to that user's message`")
    
@Annabelle.on_message(filters.command('pmpermit', HANDLER) & filters.me)
async def togglepm(Annabelle, message, PM_PERMIT):
  args = message.text.split(None, 1)
  if len(args) >= 2:
    toggle = args[1]
    if toggle.lower() in ['on', 'yes', 'true']:
      PM_PERMIT = True
      await message.edit("`PM guard turned on`")
    elif toggle.lower() in ['no', 'off', 'false']:
      PM_PERMIT = True
      await message.edit("`PM guard turned off`")
    else:
      await message.edit("`What are you saying?`")
  else:
    await message.edit("`Command incomplete`")
    
@Annabelle.on_message(filters.private & filters.incoming)
async def testpm(Annabelle, message, PM_PERMIT):
  while PM_PERMIT is True:
    id = message.from_user.id
    x = check_permit(id)
    if x is not True:
      await message.delete()
      await Annabelle.send_message(message.chat.id, PM_TEXT)
    else:
      continue
