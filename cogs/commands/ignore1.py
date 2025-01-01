import discord
from discord.ext import commands
import json

class gulzaib12(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Ignore commands"""  

    def help_custom(self):
		      emoji = '<:chat:1205955954378543165>'
		      label = "Ignore"
		      description = "Shows You Ignore Commands"
		      return emoji, label, description

    @commands.group()
    async def __Ignore__(self, ctx: commands.Context):
        """`ignore` , `ignore channel add` , `ignore channel remove`"""
       