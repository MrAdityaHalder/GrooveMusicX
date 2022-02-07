import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "5256748757:AAGnsEZbFa5xNR7WbMd3dlIzyFtIXopTjW8")
BOT_NAME = getenv("BOT_NAME", "Gʀᴏᴏᴠᴇ MᴜsɪᴄX")
API_ID = int(getenv("API_ID", "12305641"))
API_HASH = getenv("API_HASH", "c07cfe19f5fcbbeaf2d526a5863c0de3")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME", "AdityaHalder")
ALIVE_NAME = getenv("ALIVE_NAME", "Gʀᴏᴏᴠᴇ MᴜsɪᴄX")
BOT_USERNAME = getenv("BOT_USERNAME", "GrooveXrobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GrooveMusicX")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "AdityaDiscus")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AdityaServer")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
