from pyrogram import Client, __version__
from config import *
import logging

class Annabelle(Client):

    def __init__(self):
        super().__init__(
            SESSION_STRING,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict{"root": "annabelle/modules"},
        )

    async def start(self):
        await super().start()
        logging.info(f"Anabelle with for Pyrogram v{__version__} (Layer {layer}) started")
        
    async def stop(self, *args):
        await super().stop()
        logging.info("Anabelle stopped!")


app = Anabelle()
app.run()
