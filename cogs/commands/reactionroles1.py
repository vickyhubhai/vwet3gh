import discord
from discord.ext import commands


class hacker11111111111111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Reaction commands"""
  
    def help_custom(self):
		      emoji = '<:user:1205959357859373076>'
		      label = "ReactionRoles"
		      description = "Shows You Reaction Roles Commands"
		      return emoji, label, description

    @commands.group()
    async def __ReactionRoles__(self, ctx: commands.Context):
        """`reaction <emote> <role> <channel> [title=None]`"""