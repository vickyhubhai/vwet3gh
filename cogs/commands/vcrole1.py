import discord
from discord.ext import commands


class gulzaib00(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Voice commands"""
  
    def help_custom(self):
		      emoji = '<:botvoice_vaibhavs_lithium:1086460797837914163>'
		      label = "VcRoles"
		      description = "Shows You VcRoles Commands"
		      return emoji, label, description

    @commands.group()
    async def __VcRoles__(self, ctx: commands.Context):
        """`vcrole bots add` , `vcrole bots remove` , `vcrole bots` , `vcrole config` , `vcrole humans add` , `vcrole humans remove` , `vcrole humans` , `vcrole reset` , `vcrole`"""