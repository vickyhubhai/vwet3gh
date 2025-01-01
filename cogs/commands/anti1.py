import discord
from discord.ext import commands


class gulzaib1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Security commands"""
  
    def help_custom(self):
		      emoji='<:botmod2_vaibhavs_lithium:1086460199335907438>'
		      label = "AntiNuke"
		      description = "Shows You Antinuke Commands"
		      return emoji, label, description

    @commands.group()
    async def __AntiNuke__(self, ctx: commands.Context):
        """`antinuke` , `antinuke enable` , `antinuke disable` , `antinuke show` , `antinuke punishment set` , `antinuke whitelist` , `antinuke whitelist add` , `antinuke whitelist remove` , `antinuke whitelist show` , `antinuke whitelist reset` , `antinuke channelclean` , `antinuke roleclean` , `antinuke whitelist role` , `antinuke recover`"""