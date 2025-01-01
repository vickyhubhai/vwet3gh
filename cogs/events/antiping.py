import os
import discord
from discord.ext import commands
import requests
import sys
from utils.Tools import getConfig, add_user_to_blacklist, getanti
import setuptools
from itertools import cycle
from collections import Counter
import threading
import datetime
import logging
from core import Ventura, Cog
import time
import asyncio
import aiohttp
import tasksio
from discord.ui import View, Button
import json
from discord.ext import tasks
import random

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antipinginv(Cog):
    def __init__(self, client: Ventura):
        self.client = client
        self.spam_control = commands.CooldownMapping.from_cooldown(10, 12.0, commands.BucketType.user)


        

    @commands.Cog.listener()
    async def on_message(self, message):
      button = Button(emoji="<:botinvite_vaibhavs_lithium:1088838005063680100>",label="Invite", url =  "https://discord.com/api/oauth2/authorize?client_id=1205422290368725062&permissions=1513962695871&scope=bot+applications.commands")
      button1 = Button(emoji="<a:Botsupporter:1166053022225416246>",label="Support", url = "https://discord.gg/MnPsa4ZFJ3")
      button2 = Button(emoji="<a:voter:1192022649539416125>",label="Vote", url = "https://discord.gg/MnPsa4ZFJ3")
      try:
       
        with open("blacklist.json", "r") as f:
          data2 = json.load(f)
        with open('ignore.json', 'r') as heck:
          randi = json.load(heck)
          ventura = '<@1103575978770436116>'
          try:
            data = getConfig(message.guild.id)
            anti = getanti(message.guild.id)
            prefix = data["prefix"]
            wled = data["whitelisted"]
            punishment = data["punishment"]
            wlrole = data['wlrole']
            guild = message.guild
            hacker = guild.get_member(message.author.id)
            wlroles = guild.get_role(wlrole)
          except Exception:
            pass
          guild = message.guild
          if message.mention_everyone:
            if str(message.author.id) in wled or anti == "off" or wlroles in hacker.roles:
              pass
            else:
              if punishment == "ban":
                await message.guild.ban(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punishment == "kick":
                await message.guild.kick(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punishment == "none":
                return


          elif message.content == ventura or message.content == "<@!1103575978770436116>":
            if str(message.author.id) in data2["ids"]:
              embed = discord.Embed(title="<a:botcross_vaibhavs_lithium:1084877519871823972> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/MnPsa4ZFJ3)")
              await message.reply(embed=embed, mention_author=False)
            if str(message.channel.id) in randi["ids"]:
                await message.reply(f"My all commands are disabled for {message.channel.mention}",mention_author=True, delete_after=10)
                
                
            else:

              embed = discord.Embed(description=f"""\Hey, I'm Titanium

Please use the following command instead: -help

[If you continue to have problems, consider asking for help](https://discord.gg/MnPsa4ZFJ3).""",color=0x2f3136) 
              embed.set_author(name="Titanium", icon_url=self.client.user.display_avatar.url)
              embed.set_thumbnail(url =self.client.user.display_avatar.url)
              if guild.icon is not None:
                  embed.set_footer(  text=guild.name, icon_url=guild.icon.url)
              view = View()
              view.add_item(button)
              view.add_item(button1)
              view.add_item(button2)
              await message.reply(embed=embed, mention_author=False, view=view)
          else:
            return
      except Exception as error:
        if isinstance(error, discord.Forbidden):
              return






