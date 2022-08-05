import discord
from discord.ext import commands
import json
import os
with open('setting.json','r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

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
        c = bot.get_channel(int(jdata["channel"]))
        await c.send(f'{member}突然加入了我的世界!')
    
    @bot.event
    async def on_member_remove(member):
        print(f'{member}已離開我的伺服器')
        c = bot.get_channel(int(jdata["channel"]))
        await c.send(f'{member}突然離開了我的世界QQ')
    
    @bot.command()
    async def load(ctx, extension):
        bot.load_extension(F'cmds.{extension}')
        await ctx.send(F"Loaded {extension} done.")
    
    @bot.command()
    async def unload(ctx, extension):
        bot.unload_extension(F'cmds.{extension}')
        await ctx.send(F"Un - Loaded {extension} done.")
    
    @bot.command()
    async def reload(ctx, extension):
        bot.reload_extension(F'cmds.{extension}')
        await ctx.send(F"Re - Loaded {extension} done.")
    
    for Filename in os.listdir('./cmds'):
        if Filename.endswith('.py'):
            bot.load_extension(F'cmds.{Filename[:-3]}')

    if __name__=="__main__":
        bot.run(jdata["TOKEN"])