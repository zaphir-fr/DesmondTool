import keep_alive
import discord
from discord.ext import commands
import asyncio
import threading

to = input('    path to .txt ->')

TKN_FILE = (to)

class DiscordSelfBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

loop = asyncio.get_event_loop()

for TOKEN in open(TKN_FILE, "r"):
    b = DiscordSelfBot()

    loop.create_task(b.start(TOKEN, bot=False))

loop.run_forever()
keep_alive.keep_alive()
