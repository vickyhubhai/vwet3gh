import discord
from discord.ext import commands


class hacker11111111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Leveling commands"""
  
    def help_custom(self):
		      emoji = '<:leveling:1205957976481996850>'
		      label = "Levling"
		      description = "Shows You Leveling Commands"
		      return emoji, label, description

    @commands.group()
    async def __Leveling__(self, ctx: commands.Context):
        """`leveling enable` , `leveling channel <channel>` , `xp`, `leaderboard/lb`"""