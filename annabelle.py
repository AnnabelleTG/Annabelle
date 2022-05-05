from pyrogram import Client, __version__
from config import *
import logging

art = """

   _____                      ___.          .__  .__          
  /  _  \   ____   ____ _____ \_ |__   ____ |  | |  |   ____  
 /  /_\  \ /    \ /    \\__  \ | __ \_/ __ \|  | |  | _/ __ \ 
/    |    \   |  \   |  \/ __ \| \_\ \  ___/|  |_|  |_\  ___/ 
\____|__  /___|  /___|  (____  /___  /\___  >____/____/\___  >
        \/     \/     \/     \/    \/     \/               \/ 


"""

class Annabelle(Client):

    def __init__(self):
        super().__init__(
            SESSION_STRING,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins={"root": "annabelle/modules"},
        )

    async def start(self):
        await super().start()
        print(art)
        logging.info(f"Anabelle with for Pyrogram v{__version__} (Layer {layer}) started")
        
    async def stop(self, *args):
        await super().stop()
        logging.info("Anabelle stopped!")


app = Anabelle()
app.run()
