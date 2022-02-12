from pyrogram.types import Message


def ReplyCheck(message:Message):
  reply_id = None

  if message.reply_to_message:
    reply_id = message.reply_to_message.message_id
  
  elif not message.from_user.is_self:
    reply_id = message.message_id
  
  return reply_id

def GetChatID(message: Message):
    """ Get the group id of the incoming message"""
    return message.chat.id
