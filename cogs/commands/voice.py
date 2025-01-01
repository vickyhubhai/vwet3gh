import discord
from discord.ext import commands


class shree00(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Voice commands"""
  
    def help_custom(self):
		      emoji = '<:botvoice_vaibhavs_lithium:1086460797837914163>'
		      label = "Voice"
		      description = "Shows You Voice Commands"
		      return emoji, label, description

    @commands.group()
    async def __Voice__(self, ctx: commands.Context):
        """`voice` , `voice kick` , `voice kickall` , `voice mute` , `voice muteall` , `voice unmute` , `voice unmuteall` , `voice deafen` , `voice deafenall` , `voice undeafen` , `voice undeafenall` , `voice moveall`"""






