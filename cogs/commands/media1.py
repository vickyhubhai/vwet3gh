import discord
from discord.ext import commands


class hacker111111111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Media commands"""
  
    def help_custom(self):
		      emoji = '<:SocialMedia:1205956834180210819>'
		      label = "Media"
		      description = "Shows You Media Commands"
		      return emoji, label, description

    @commands.group()
    async def __Media__(self, ctx: commands.Context):
        """`media` , `media setup <channel>` , `media remove <channel>`, `media config`"""