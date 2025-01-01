import discord
from discord.ext import commands


class shree1227(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Raidmode commands"""
  
    def help_custom(self):
		      emoji = '<:botautomod_vaibhavs_lithium:1086466405819494521>'
		      label = "Raidmode"
		      description = "Shows You Raidmode Commands"
		      return emoji, label, description

    @commands.group()
    async def __Automod__(self, ctx: commands.Context):
        """`automod` , `antispam on` , `antispam off` , `antilink off` ,  `antilink on`"""