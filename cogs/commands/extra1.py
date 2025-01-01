import discord
from discord.ext import commands


class gulzaib2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Extra commands"""
  
    def help_custom(self):
		      emoji = '<:botsettings_vaibhavs_lithium:1166043399971950713>'
		      label = "Utility"
		      description = "Shows You Utility Commands"
		      return emoji, label, description

    @commands.group()
    async def __Utility__(self, ctx: commands.Context):
        """`stats` , `invite` , `serverinfo` , `userinfo` , `roleinfo` , `botinfo` , `status` , `emoji` , `user` , `role` , `channel` , `boosts`, `emoji-add` , `removeemoji` , `unbanall` ,  `joined-at` , `ping` , `github` , `vcinfo` , `channelinfo` , `note` , `notes` , `trashnotes` , `badges` , `ignore` , `ignore channel` , `ignore channel add` , `ignore channel remove` , `banner user` , `banner server`"""