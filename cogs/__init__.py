from __future__ import annotations
from core import Ventura

#____________ Commands ___________

#####################3
from .commands.help import Help
from .commands.general import General
from .commands.music import Music
from .commands.moderation import Moderation
from .commands.anti import Security
from .commands.raidmode import Automod
from .commands.welcome import Welcomer
from .commands.fun import Fun
from .commands.Games import Games
from .commands.extra import Utility
from .commands.owner import Owner
from .commands.vcroles import Voice
from .commands.role import Server
from .commands.ignore import Ignore
from .commands.vanityroles import Vanityroles
from .commands.ticket import Ticket
from .commands.jsk import Jsk
from .commands.encryption import Encryption
from .commands.fun import Fun
from .commands.Verification import Verification
from .commands.media import Media
from .commands.nsfw import Nsfw
from .commands.jsk import Jsk
from .commands.Leveling import Leveling
from .commands.reactionroles import ReactionRoles
from .commands.Afk import afk
from .commands.pfps import pfps
from .commands.Giveaways import give
from .commands.giveaway_task import gwtask

#____________ Events _____________
from .events.antiban import antiban
from .events.antichannel import antichannel
from .events.antiguild import antiguild
from .events.antirole import antirole
from .events.antibot import antibot
from .events.antikick import antikick
from .events.antiprune import antiprune
from .events.antiwebhook import antiwebhook
from .events.antiping import antipinginv
from .events.antiemostick import antiemostick
from .events.antintegration import antintegration
from .events.antispam import AntiSpam
from .events.autoblacklist import AutoBlacklist
from .events.antiemojid import antiemojid
from .events.antiemojiu import antiemojiu
from .events.Errors import Errors
from .events.on_guild import Guild
from .events.autorole import Autorole2
from .events.greet2 import greet
from .events.voiceupdate import Vcroles2

##############33cogs#############
from .commands.anti1 import gulzaib1
from .commands.general1 import gulzaib102
from .commands.music1 import shree3110
from .commands.raidmode1 import shree1227
from .commands.welcome1 import gulzaibshree3110
from .commands.vanityroles1 import gulzaib7
from .commands.ticket1 import gulzaib16
from .commands.server import gulzaib1227
from .commands.mod2 import gulzaib3110
from .commands.games1 import gulzaib96
from .commands.owner1 import hacker1111111111111111111111
from .commands.extra1 import gulzaib2
from .commands.voice import shree00
from .commands.vcrole1 import gulzaib00
from .commands.ignore1 import gulzaib12
from .commands.encryption1 import gulzaib15
from .commands.fun1 import gulzaib69
from .commands.verification1 import ver1
from .commands.media1 import hacker111111111111111
from .commands.nsfw1 import shree2712
from .commands.jsk1 import gulzaib13
from .commands.Leveling1 import hacker11111111111111
from .commands.reactionroles1 import hacker11111111111111111111
from .commands.pfps1 import pfps1
from .commands.gw1 import gw1


async def setup(bot: Astroz):
  await bot.add_cog(Help(bot))
  await bot.add_cog(General(bot))
  await bot.add_cog(Music(bot))
  await bot.add_cog(Moderation(bot))
  await bot.add_cog(Security(bot))
  await bot.add_cog(Automod(bot))
  await bot.add_cog(Welcomer(bot))
  await bot.add_cog(Fun(bot))
  await bot.add_cog(Games(bot))
  await bot.add_cog(Utility(bot))
  await bot.add_cog(Voice(bot))
  await bot.add_cog(Owner(bot))
  await bot.add_cog(Server(bot))
  await bot.add_cog(Vanityroles(bot))
  await bot.add_cog(Ticket(bot))
  await bot.add_cog(Ignore(bot))
  await bot.add_cog(Encryption(bot))
  await bot.add_cog(Verification(bot))
  await bot.add_cog(Media(bot))
  await bot.add_cog(Nsfw(bot))
  await bot.add_cog(Jsk(bot))
  await bot.add_cog(Leveling(bot))
  await bot.add_cog(ReactionRoles(bot))
  await bot.add_cog(afk(bot))
  await bot.add_cog(pfps(bot))
  await bot.add_cog(give(bot))
  await bot.add_cog(gwtask(bot))

  ####################

  await bot.add_cog(gulzaib1(bot))
  await bot.add_cog(gulzaib102(bot))
  await bot.add_cog(shree3110(bot))
  await bot.add_cog(shree1227(bot))
  await bot.add_cog(gulzaibshree3110(bot))
  await bot.add_cog(gulzaib7(bot))
  await bot.add_cog(gulzaib16(bot))
  await bot.add_cog(hacker1111111111111111111111(bot))
  await bot.add_cog(hacker111111111111111(bot))
  await bot.add_cog(gulzaib1227(bot))
  await bot.add_cog(gulzaib3110(bot))
  await bot.add_cog(gulzaib96(bot))
  await bot.add_cog(gulzaib2(bot))
  await bot.add_cog(shree00(bot))
  await bot.add_cog(gulzaib00(bot))
  await bot.add_cog(shree2712(bot))
  await bot.add_cog(gulzaib12(bot))
  await bot.add_cog(gulzaib15(bot))
  await bot.add_cog(gulzaib69(bot))
  await bot.add_cog(ver1(bot))
  await bot.add_cog(gulzaib13(bot))
  await bot.add_cog(hacker11111111111111111111(bot))
  await bot.add_cog(hacker11111111111111(bot))
  await bot.add_cog(pfps1(bot))
  await bot.add_cog(gw1(bot))

  ###########################events################3

  await bot.add_cog(antiban(bot))
  await bot.add_cog(antichannel(bot))
  await bot.add_cog(antiguild(bot))
  await bot.add_cog(antirole(bot))
  await bot.add_cog(antibot(bot))
  await bot.add_cog(antikick(bot))
  await bot.add_cog(antiprune(bot))
  await bot.add_cog(antiwebhook(bot))
  await bot.add_cog(antipinginv(bot))
  await bot.add_cog(antiemostick(bot))
  await bot.add_cog(antintegration(bot))
  await bot.add_cog(AntiSpam(bot))
  await bot.add_cog(AutoBlacklist(bot))
  await bot.add_cog(antiemojid(bot))
  await bot.add_cog(antiemojiu(bot))
  await bot.add_cog(Guild(bot))
  await bot.add_cog(Errors(bot))
  await bot.add_cog(Autorole2(bot))
  await bot.add_cog(greet(bot))
  await bot.add_cog(Vcroles2(bot))
