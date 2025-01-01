import discord
from discord.ext import commands
import json

class j2c(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """J2C commands"""

    def help_custom(self):
		      emoji ='<:botvoice_vaibhavs_lithium:1086460797837914163> '
		      label = "Join To Create"
		      description = "・ shows join to create cmds"
		      return emoji, label, description
#')

    # now make a command where the server owner can change the channel for leveling.
    @commands.group()
    async def J2C(self, ctx: commands.Context):
        """**```j2c, j2c allow, j2c channel, j2c claim, j2c deny, j2c hide, j2c limit, j2c lock, j2c name, j2c setlimit, j2c setup, j2c unhide, j2c unlock```"""
       # await ctx.send('leveling is under construction.')
    

    
    #@commands.command()
    ##async def level(self, ctx: commands.Context, user: discord.Member):
     #   with open('./data/databases/leveling.json', 'r') as f:
           # leveling = json.load(f)
       # await ctx.send(f'{user.mention} is currently level {leveling[str(user.id)]["level"]}.')

def setup(bot):
    bot.add_cog(j2c(bot))