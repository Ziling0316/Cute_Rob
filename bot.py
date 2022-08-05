import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
import random
while True:
    bot = commands.Bot(command_prefix ='!', intents = intents)
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
    @bot.command()
    async def 炫炮機器人(ctx):
        await ctx.send("哈囉我在呦")
    #@bot.command()
    #async def ping(ctx):
        #await ctx.send(f'{round(bot.latency*1000)}(ms)')
    @bot.command()
    async def 圖片(ctx):
        pic = discord.File('C:\\Users\\jolin\\OneDrive\\桌面\\Cute_Rob\\picture.png')
        await ctx.send(file = pic)
    @bot.command()
    async def 抽籤(ctx):
        choose = [1, 2, 3, 4]
        random_num = random.choice(choose)
        if random_num == 1:
            await ctx.send("大吉領紅茶")
        elif random_num == 2:
            await ctx.send("中吉之三國")
        elif random_num == 3:
            await ctx.send("大凶部姐姐")
        elif random_num == 4:
            await ctx.send("你今天普普")
    
    bot.run("MTAwNDY4NTgzNjY4OTg4MzE5Ng.Geeqym.8fFmD0qMmBdlycaZ9Oo3eVEMl8j0qPYdBV6DMk")