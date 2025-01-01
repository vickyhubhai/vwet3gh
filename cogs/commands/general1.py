import discord
from discord.ext import commands


class gulzaib102(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """General commands"""
  
    def help_custom(self):
		      emoji ='<:botantinuke_vaibhavs_lithium:1084877441920675920>'
		      label = "General"
		      description = "Shows You General Commands"
		      return emoji, label, description
    @commands.group()
    async def __General__(self, ctx: commands.Context):
        """`afk` , `avatar` , `banner` , `servericon` , `membercount` , `poll` , `hack` , `token` , `users` , `italicize` , `strike` , `quote` , `code` , `bold` , `censor` , `underline` , `gender` , `wizz` , `pikachu` , `shorten` , `urban` , `rickroll` , `hash` , `snipe` , `roleall`"""