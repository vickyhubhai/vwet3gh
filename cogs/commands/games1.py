import discord
from discord.ext import commands


class gulzaib96(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Games commands"""
  
    def help_custom(self):
		      emoji = '<:botgames_vaibhavs_lithium:1086460417020272781>'
		      label = "Games"
		      description = "Shows You Games Commands"
		      return emoji, label, description

    @commands.group()
    async def __Games__(self, ctx: commands.Context):
        """`akinator` , `chess` , `hangman` , `typerace` , `rps` , `reaction` , `tick-tack-toe` , `wordle` , `2048` , `memory-game` , `number-slider` , `battleship` , `country-guesser`"""