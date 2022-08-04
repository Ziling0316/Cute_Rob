import discord
from discord.ext import commands
while True:
    bot = commands.Bot(command_prefix ='$')
    @bot.event
    async def on_ready():
        print(">> Bot is online <<")

    bot.run("MTAwNDY4NTgzNjY4OTg4MzE5Ng.Gk8M-A.yLMjSGKbi7PWNY4sf86RGvVxXc8jSfaG-aa7lE")