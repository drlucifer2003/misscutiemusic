import requests
from pyrogram import idle
from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

async def main():
    async with bot:
        try:
            await USER.join_chat(misscuitesupport)
            await USER.join_chat(misscuiteupdate)
        except UserAlreadyParticipant:
            pass
        except Exception as e:
            print(e)
            pass

bot.start()
run()
idle()
