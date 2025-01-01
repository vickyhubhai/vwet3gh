import discord
from discord.ext import commands


class hacker1111111111111111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Owner commands"""
  
    def help_custom(self):
		      emoji = '<:ownership:1192023643224539156>'
		      label = "Owner"
		      description = "Shows You Owner Commands"
		      return emoji, label, description

    @commands.group()
    async def __Owner__(self, ctx: commands.Context):
        """`eval` , `slist` , `restart` , `sync` , `np` , `np add` , `np remove` , `np list` , `bl show` , `bl add` , `bl remove` , `bdg` , `bdg add` , `bdg remove` , `dm` , `nick` , `globalban` , `playing` , `streaming` , `watching` , `competing` , `listening` , apre"""