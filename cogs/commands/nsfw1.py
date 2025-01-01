import discord
from discord.ext import commands

class shree2712(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """NSFW commands"""
  
    def help_custom(self):
		      emoji = '<:botnsfw_vaibhavs_lithium:1084878161227030689>'
		      label = "Nsfw"
		      description = "Shows You Nsfw Commands"
		      return emoji, label, description

    @commands.group()
    async def __Nsfw__(self, ctx: commands.Context):
        """`nsfw` , `nsfw 4k` , `nsfw pussy` , `nsfw boobs` , `nsfw lewd` , `nsfw lesbian` , `nsfw blowjob` , `nsfw cum` , `nsfw gasm` , `nsfw hentai`"""