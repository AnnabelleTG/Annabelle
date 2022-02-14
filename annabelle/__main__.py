import userbot
from userbot import Annabelle
from userbot import scheduler

if __name__ == "__main__":
    userbot.client = Annabelle

    scheduler.start()

    Annabelle.run()
