import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
while True:
    bot = commands.Bot(command_prefix ='[', intents = intents)
    @bot.event
    async def on_ready():
        print(">> Bot is online <<")
    @bot.event
    async def on_member_join(member):
        print(f'{member}已加入我的伺服器')
        c = bot.get_channel(1004680247372951595)
        await c.send(f'{member}突然加入了我的世界!')
    @bot.event
    async def on_member_remove(member):
        print(f'{member}已離開我的伺服器')
        c = bot.get_channel(1004680247372951595)
        await c.send(f'{member}突然離開了我的世界QQ')

    bot.run("MTAwNDY4NTgzNjY4OTg4MzE5Ng.GkglTM.SY4B8u7633rgPzjuE3bpudXMay6UiNaO9hEmSA")