import discord
from discord.ext import commands


class gulzaib69(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Fun commands"""
  
    def help_custom(self):
		      emoji = '<:botfun_vaibhavs_lithium:1084877600385667202>'
		      label = "Fun"
		      description = "Shows You Fun Commands"
		      return emoji, label, description

    @commands.group()
    async def __Fun__(self, ctx: commands.Context):
        """` tickle` , `kiss` , `hug` , `slap` , `pat` , `feed` , `pet` , `howgay` , `slots` , ` penis` , `meme` , `cat` , `iplookup`"""