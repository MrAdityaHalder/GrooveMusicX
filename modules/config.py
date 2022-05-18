import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
API_ID = int(getenv("API_ID", "12305641"))
API_HASH = getenv("API_HASH", "c07cfe19f5fcbbeaf2d526a5863c0de3")
STRING_SESSION = getenv("STRING_SESSION", "AQARkMowCMdN2r-htiCdxycC_TTwvnhFQc9WviRq1FOKXJyO960LxlaXH3Arrp-LatYI7s3WJtafUmSl1MBXNmmQMAmcJOzERNnON_piJP8IK4QeWWgniwwwxQlCdbHAK3638hJJV6jj7yU6RiWSf96733nRdO5jADSjwTX4HpMnVIvVWH75z3mldeRUcpx5_2XxFQXZjzwMevCZlCYOj4M2XOE68PHe8OJQ9c9mZoS12uU1tgk9UkEr6b3D8EoBMQH0cDL7MymcwVQY3NQQxXtAv02bdnDjhTZAiLYZnXhXaYBWzWRFr602SZBgelCfPQ3g2SJYnU02yNdq6jrIXhHRAAAAATh6bN0A")
ALIVE_NAME = getenv("ALIVE_NAME", "Gʀᴏᴏᴠᴇ MᴜsɪᴄX")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GrooveMusicX")
BOT_NAME = getenv("BOT_NAME", "Gʀᴏᴏᴠᴇ MᴜsɪᴄX")
BOT_USERNAME = getenv("BOT_USERNAME", "GrooveXrobot")
BOT_TOKEN = getenv("BOT_TOKEN", "5256748757:AAGnsEZbFa5xNR7WbMd3dlIzyFtIXopTjW8")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
OWNER_NAME = getenv("OWNER_NAME", "Aditya Halder")
OWNER_USERNAME = getenv("OWNER_USERNAME", "adityahalder")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "adityaserver")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "adityadiscus")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/mradityahalder/groovemusicx")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")
