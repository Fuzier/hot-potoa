import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import asyncio
import os
import sys

interval = 3
timer = 6
zad = 60 * 5

currentTime = time.time()

Bot = commands.Bot(command_prefix= '.')

take = ['поймал', 'словил']
commands = ['.картошка']

@Bot.event
async def on_ready():
    print("Bot is online")

@Bot.command( pass_context = True )
async def картошка(ctx, member = ''):
    channel = Bot.get_channel(707981325591773215)

    await channel.send("Таймер на 5 минут начался, быстрее пиши \".поймал\"!")
    await asyncio.sleep(300)
    await channel.send("К сожалению ты проиграл :(")
@Bot.command( pass_context = True )
async def поймал(ctx):
    channel = Bot.get_channel(707981325591773215)      
    await channel.send("Молодец! Ты продолжаешь учавствовать в игре :)")
    os.execl(sys.executable, sys.executable, *sys.argv) 
    
token = os.environ.get('BOT_TOKEN')
