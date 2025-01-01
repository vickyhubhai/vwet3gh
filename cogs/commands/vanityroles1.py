import discord
from discord.ext import commands


class gulzaib7(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Vanityroles commands"""
  
    def help_custom(self):
		      emoji = '<a:vanity:1198657062956179566>'
		      label = "Vanityroles"
		      description = "Shows You Vanityroles Commands"
		      return emoji, label, description

    @commands.group()
    async def __Vanityroles__(self, ctx: commands.Context):
        """`vanityroles` , `vanityroles show` , `vanityroles config` , `vanityroles reset` , `vanityroles setup`"""