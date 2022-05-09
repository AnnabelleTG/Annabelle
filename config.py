import os
from os import environ

# vars that need to run the bot
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
SESSION_STRING = environ['SESSION_STRING']
BOT_TOKEN = environ['BOT_TOKEN']
HANDLER = environ.get(('HANDLER'))
MY_ID = int(environ.get('MY_ID'))
SUDO_USERS = environ.get('SUDO_USERS', MY_ID).split()
DATABASE_NAME = str(environ.get('DATABASE_NAME'))
DATABASE_URL = environ.get('DATABASE_URL')
CHANNEL_ID = environ.get('CHANNEL_ID')
CMD_HELP = {}
