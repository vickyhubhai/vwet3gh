import discord
from discord.ext import commands


class shree3110(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Music commands"""
  
    def help_custom(self):
		      emoji = '<a:vaibhav_music_vaibhavs_lithium:1166256651603550228>'
		      label = "Music"
		      description = "Shows You Music Commands"
		      return emoji, label, description

    @commands.group()
    async def __Music__(self, ctx: commands.Context):
        """`play` , `connect` , `disconnect` , `stop` , `skip`   ,  `pause` ,  `resume` , `bassboost`  , `move` , `volume` , `nowplaying` , `shuffle` , `pull` , `queue` , `queue clear` , `seek`"""