from os import path, mkdir
from sys import stdout
from datetime import datetime
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
from annabelle import Annabelle

LOG_DATETIME = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
LOGDIR = f"{__name__}/logs"

if not path.isdir(LOGDIR):
    mkdir(LOGDIR)

LOGFILE = f"{LOGDIR}/{__name__}_{LOG_DATETIME}_log.txt"

file_handler = FileHandler(filename=LOGFILE)
stdout_handler = StreamHandler(stdout)

basicConfig(
    format="%(asctime)s - [Annabelle] - %(levelname)s - %(message)s",
    level=INFO,
    handlers=[file_handler, stdout_handler],
)

getLogger("pyrogram").setLevel(WARNING)
logger = getLogger(__name__)



app = Annabelle()
app.run()
