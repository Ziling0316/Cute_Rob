import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 炫炮機器人(ctx):
        await ctx.send("哈囉我在呦")
    @commands.command()
    async def 圖片(self, ctx):
        choose = [1, 2]
        random_int = random.choice(choose)
        if random_int == 1:
            pic = discord.File('C:\\Users\\jolin\\OneDrive\\桌面\\Cute_Rob\\picture.png')
            await ctx.send(file = pic)
        else:
            pic = discord.File('C:\\Users\\jolin\\OneDrive\\桌面\\Cute_Rob\\picture2.png')
            await ctx.send(file = pic)
    @commands.command()
    async def 抽籤(self, ctx):
        choose = [1, 2, 3, 4]
        random_num = random.choice(choose)
        if random_num == 1:
            await ctx.send("大吉領紅茶")
        elif random_num == 2:
            await ctx.send("中吉之三國")
        elif random_num == 3:
            await ctx.send("大凶部姐姐")
        else:
            await ctx.send("你今天普普")

def setup(bot):
    bot.add_cog(React(bot))