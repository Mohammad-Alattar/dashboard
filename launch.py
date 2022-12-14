import os
import discord
from prisma.utils import async_run
from bot import MainBot
from helpers.prefix import prefix_bot
from discord.ext import ipc
bot = MainBot(
    command_prefix=prefix_bot,
    description="Bot.",
    case_insensitive=True,
    intents=discord.Intents.all()
)
if "__main__" == __name__:
    async_run(bot.prisma.connect())
    bot.run(os.environ["BOT_TOKEN"])