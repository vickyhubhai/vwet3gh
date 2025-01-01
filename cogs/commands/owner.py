from __future__ import annotations
from discord.ext import commands
from utils.Tools import *
from discord import *
from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator

from typing import Optional


class Owner(commands.Cog):

  def __init__(self, client):
    self.client = client

  def help_custom(self):
    emoji = '<:ownership:1192023643224539156>'
    label = "Owner"
    description = "Shows You Developer Commands"
    return emoji, label, description

  @commands.command(name="slist")
  @commands.is_owner()
  async def _slist(self, ctx):
    hasanop = ([hasan for hasan in self.client.guilds])
    hasanop = sorted(hasanop,
                     key=lambda hasan: hasan.member_count,
                     reverse=True)
    entries = [
      f"`[{i}]` | [{g.name}](https://discord.com/channels/{g.id}) - {g.member_count}"
      for i, g in enumerate(hasanop, start=1)
    ]
    paginator = Paginator(source=DescriptionEmbedPaginator(
      entries=entries,
      description="",
      title=f"Titanium Server List - {len(self.client.guilds)}",
      color=0x2f3136,
      per_page=10),
                          ctx=ctx)
    await paginator.paginate()

  @commands.command(name="restart", help="Restarts the client.")
  @commands.is_owner()
  async def _restart(self, ctx: Context):
    await ctx.reply("Restarting!")
    restart_program()

  @commands.command(name="sync", help="Syncs all database.")
  @commands.is_owner()
  async def _sync(self, ctx):
    await ctx.reply("Syncing...", mention_author=False)
    with open('anti.json', 'r') as f:
      data = json.load(f)
    for guild in self.client.guilds:
      if str(guild.id) not in data['guild']:
        data['guilds'][str(guild.id)] = 'on'
        with open('anti.json', 'w') as f:
          json.dump(data, f, indent=4)
      else:
        pass
    with open('config.json', 'r') as f:
      data = json.load(f)
    for op in data["guilds"]:
      g = self.client.get_guild(int(op))
      if not g:
        data["guilds"].pop(str(op))
        with open('config.json', 'w') as f:
          json.dump(data, f, indent=4)

  @commands.group(name="blacklist",
                  help="let's you add someone in blacklist",
                  aliases=["bl"])
  @commands.is_owner()
  async def blacklist(self, ctx):
    if ctx.invoked_subcommand is None:
      with open("blacklist.json") as file:
        blacklist = json.load(file)
        entries = [
          f"`[{no}]` | <@!{mem}> (ID: {mem})"
          for no, mem in enumerate(blacklist['ids'], start=1)
        ]
        paginator = Paginator(source=DescriptionEmbedPaginator(
          entries=entries,
          title=
          f"List of Blacklisted users of Titanium - {len(blacklist['ids'])}",
          description="",
          per_page=10,
          color=0x2f3136),
                              ctx=ctx)
        await paginator.paginate()

  @blacklist.command(name="add")
  @commands.is_owner()
  async def blacklist_add(self, ctx: Context, member: discord.Member):
    try:
      with open('blacklist.json', 'r') as bl:
        blacklist = json.load(bl)
        if str(member.id) in blacklist["ids"]:
          embed = discord.Embed(
            title="Error!",
            description=f"{member.name} is already blacklisted",
            color=discord.Colour(0x2f3136))
          await ctx.reply(embed=embed, mention_author=False)
        else:
          add_user_to_blacklist(member.id)
          embed = discord.Embed(
            title="User Blacklisted",
            description=
            f"{member.name} has been successfully added to blacklist",
            color=discord.Colour(0x2f3136))
          with open("blacklist.json") as file:
            blacklist = json.load(file)
            embed.set_footer(
              text=
              f"There are now {len(blacklist['ids'])} users in the blacklist")
            await ctx.reply(embed=embed, mention_author=False)
    except:
      embed = discord.Embed(title="Error!",
                            description=f"An Error Occurred",
                            color=discord.Colour(0x2f3136))
      await ctx.reply(embed=embed, mention_author=False)

  @blacklist.command(name="remove")
  @commands.is_owner()
  async def blacklist_remove(self, ctx, member: discord.Member = None):
    try:
      remove_user_from_blacklist(member.id)
      embed = discord.Embed(
        title="User removed from blacklist",
        description=f"{member.name} has been removed from the blacklist",
        color=0x2f3136)
      with open("blacklist.json") as file:
        blacklist = json.load(file)
        embed.set_footer(
          text=f"There are now {len(blacklist['ids'])} users in the blacklist")
        await ctx.reply(embed=embed, mention_author=False)
    except:
      embed = discord.Embed(
        title="Error!",
        description=f"**{member.name}** is not in the blacklist.",
        color=0x2f3136)
      embed.set_thumbnail(url=f"{self.client.user.display_avatar.url}")
      await ctx.reply(embed=embed, mention_author=False)

  @commands.group(
    name="np",
    help="Allows you to add someone in no prefix list (owner only command)")
  @commands.is_owner()
  async def _anp(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(ctx.command)

  @_anp.command(name="list")
  @commands.is_owner()
  async def anp_list(self, ctx):
    with open("info.json") as f:
      np = json.load(f)
      nplist = np["np"]
      npl = ([await self.client.fetch_user(nplu) for nplu in nplist])
      npl = sorted(npl, key=lambda nop: nop.created_at)
      entries = [
        f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) (ID: {mem.id})"
        for no, mem in enumerate(npl, start=1)
      ]
      paginator = Paginator(source=DescriptionEmbedPaginator(
        entries=entries,
        title=f"No Prefix of Titanium - {len(nplist)}",
        description="",
        per_page=10,
        color=0x2f3136),
                            ctx=ctx)
      await paginator.paginate()

  @_anp.command(name="add", help="Add user to no prefix")
  @commands.is_owner()
  async def anp_add(self, ctx, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id in np:
      embed = discord.Embed(
        description=f"**The User You Provided Already In My No Prefix**",
        color=0x2f3136)
      await ctx.reply(embed=embed)
      return
    else:
      data["np"].append(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      embed1 = discord.Embed(
        description=f"<a:tick_vaibhavs_lithium:1166037808868237364> | Added no prefix to {user}",
        color=0x2f3136)

      await ctx.reply(embed=embed1)

  @_anp.command(name="remove", help="Remove user from no prefix")
  @commands.is_owner()
  async def anp_remove(self, ctx, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id not in np:
      embed = discord.Embed(
        description="**{} is not in no prefix!**".format(user), color=0x2f3136)
      await ctx.reply(embed=embed)
      return
    else:
      data["np"].remove(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      embed2 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | Removed no prefix from {user}",
        color=0x2f3136)

      await ctx.reply(embed=embed2)

  @commands.group(name="bdg", help="Allows owner to add badges for a user")
  @commands.is_owner()
  async def _badge(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(ctx.command)

  @_badge.command(name="add",
                  aliases=["give"],
                  help="Add some badges to a user.")
  @commands.is_owner()
  async def badge_add(self, ctx, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["dev", "developer", "devp"]:
      idk = "**<a:Developer_vaibhavs_lithium:1197550043771711599>・DEVELOPER**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed2 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `Developer` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed2)
    elif badge.lower() in ["king", "owner"]:
      idk = "**<:ownership:1192023643224539156>・OWNER**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed8 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `OWNER` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed8)
    elif badge.lower() in ["admin", "ad"]:
      idk = "**<:admin_vaibhavs_lithium:1197549602015031428>・ADMIN**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed20 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `ADMIN` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed20)
    elif badge.lower() in ["mod", "moderator"]:
      idk = "**<:mod_badge:1197551931384676373>・MODERATOR**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed15 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `MODERATOR` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed15)

    elif badge.lower() in ["staff", "support staff"]:
      idk = "**<:Staff:1197552141624148012>・STAFF**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed3 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `STAFF` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed3)
    elif badge.lower() in ["partner"]:
      idk = "**<:partnership:1197551140255039489>・PARTNER**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed4 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `PARTNER` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed4)
    elif badge.lower() in ["sponser"]:
      idk = "**<a:premium_vaibhavs_lithium:1192020095413780562>・SPONSER**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed5 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `SPONSER` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed5)
    elif badge.lower() in ["friend", "friends", "homies", "owner's friend"]:
      idk = "**<:partnership:1197551140255039489>・FRIENDS**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed1 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `FRIENDS` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed1)
    elif badge.lower() in ["early", "supporter", "support"]:
      idk = "**<a:earlysupporter:1197552339695972382>・SUPPORTER**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed6 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `SUPPORTER` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed6)

    elif badge.lower() in ["vip"]:
      idk = "**<:dc_Vipz:1197551333797019799>・VIP**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed7 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `VIP` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed7)

    elif badge.lower() in ["bug", "hunter"]:
      idk = "**<:BugHunter:1199026962958647487>・BUG HUNTER**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed8 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `BUG HUNTER` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed8)
    elif badge.lower() in ["all"]:
      idk = "**<a:Developer_vaibhavs_lithium:1197550043771711599>・DEVELOPER\n<:ownership:1192023643224539156>・OWNER\n<:admin_vaibhavs_lithium:1197549602015031428>・ADMIN\n<:mod_badge:1197551931384676373>・MODERATOR\n<:Staff:1197552141624148012>・STAFF\n<:partnership:1197551140255039489>・PARTNER\n<a:premium_vaibhavs_lithium:1192020095413780562>・SPONSER\n<:partnership:1197551140255039489>・FRIENDS\n<a:earlysupporter:1197552339695972382>・SUPPORTER\n<:dc_Vipz:1197551333797019799>・VIP\n<:BugHunter:1199026962958647487>・BUG HUNTER**"
      ok.append(idk)
      makebadges(member.id, ok)
      embedall = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Added `All` Badges To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embedall)
    else:
      hacker = discord.Embed(description="**Invalid Badge**", color=0x2f3136)

      await ctx.reply(embed=hacker)

  @_badge.command(name="remove",
                  help="Remove badges from a user.",
                  aliases=["re"])
  @commands.is_owner()
  async def badge_remove(self, ctx, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["dev", "developer", "devp"]:
      idk = "**<a:Developer_vaibhavs_lithium:1197550043771711599>・DEVELOPER**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed2 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `Developer` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed2)
    elif badge.lower() in ["king", "owner"]:
      idk = "**<:ownership:1192023643224539156>・OWNER**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed8 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `OWNER` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed8)
    elif badge.lower() in ["admin", "ad"]:
      idk = "**<:admin_vaibhavs_lithium:1197549602015031428>・ADMIN**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed20 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `ADMIN` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed20)
    elif badge.lower() in ["mods", "moderator"]:
      idk = "**<:mod_badge:1197551931384676373>・MODERATOR**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed15 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `MODERATOR` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed15)

    elif badge.lower() in ["staff", "support staff"]:
      idk = "**<:Staff:1197552141624148012>・STAFF**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed3 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `STAFF` Badge To {member}**",
        color=0x2f3136)
      await ctx.reply(embed=embed3)
    elif badge.lower() in ["partner"]:
      idk = "**<:partnership:1197551140255039489>・PARTNER**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed4 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `PARTNER` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed4)
    elif badge.lower() in ["sponsor"]:
      idk = "**<a:premium_vaibhavs_lithium:1192020095413780562>・SPONSER**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed5 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `SPONSER` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed5)
    elif badge.lower() in ["friend", "friends", "homies", "owner's friend"]:
      idk = "**<:partnership:1197551140255039489>・FRIENDS**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed1 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `FRIENDS` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed1)
    elif badge.lower() in ["early", "supporter", "support"]:
      idk = "**<a:earlysupporter:1197552339695972382>・SUPPORTER**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed6 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `SUPPORTER` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed6)

    elif badge.lower() in ["vip"]:
      idk = "**<:dc_Vipz:1197551333797019799>・VIP**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed7 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `VIP` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed7)

    elif badge.lower() in ["bug", "hunter"]:
      idk = "**<:BugHunter:1199026962958647487>・BUG HUNTER**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed8 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `BUG HUNTER` Badge To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embed8)
    elif badge.lower() in ["all"]:
      idk = "**<a:Developer_vaibhavs_lithium:1197550043771711599>・DEVELOPER\n<:ownership:1192023643224539156>・OWNER\n<:admin_vaibhavs_lithium:1197549602015031428>・ADMIN\n<:mod_badge:1197551931384676373>・MODERATOR\n<:Staff:1197552141624148012>・STAFF\n<:partnership:1197551140255039489>・PARTNER\n<a:premium_vaibhavs_lithium:1192020095413780562>・SPONSER\n<:partnership:1197551140255039489>・FRIENDS\n<a:earlysupporter:1197552339695972382>・SUPPORTER\n<:dc_Vipz:1197551333797019799>・VIP\n<:BugHunter:1199026962958647487>・BUG HUNTER**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embedall = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | **Successfully Removed `All` Badges To {member}**",
        color=0x2f3136)

      await ctx.reply(embed=embedall)
    else:
      hacker = discord.Embed(description="**Invalid Badge**", color=0x2f3136)
      await ctx.reply(embed=hacker)

  @commands.command()
  @commands.is_owner()
  async def dm(self, ctx, user: discord.User, *, message: str):
    """ DM the user of your choice """
    try:
      await user.send(message)
      await ctx.send(
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully Sent a DM to **{user}**")
    except discord.Forbidden:
      await ctx.send(
        "This user might be having DMs blocked or it's a bot account...")

  @commands.group()
  @commands.is_owner()
  async def change(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(str(ctx.command))

  @change.command(name="nickname")
  @commands.is_owner()
  async def change_nickname(self, ctx, *, name: str = None):
    """ Change nickname. """
    try:
      await ctx.guild.me.edit(nick=name)
      if name:
        await ctx.send(
          f"<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully changed nickname to **{name}**"
        )
      else:
        await ctx.send(
          "<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully removed nickname")
    except Exception as err:
      await ctx.send(err)

  @commands.command()
  @commands.is_owner()
  async def globalban(self, ctx, *, user: discord.User = None):
    if user is None:
      return await ctx.send("You need to define the user")
    for guild in self.client.guilds:
      for member in guild.members:
        if member == user:
          await user.ban(reason="lu*d le lo")

  @commands.is_owner()
  @commands.command(help="Change the bot's status")
  async def changestatus(self, ctx: commands.Context, *, status: str):
    await self.client.change_presence(activity=discord.Game(name=status),
                                      status=discord.Status.online)
    await ctx.message.add_reaction('<a:tick_vaibhavs_lithium:1166037808868237364>')

  @commands.is_owner()
  @commands.command(help="Change the bot's status")
  async def listening(self, ctx: commands.Context, *, status: str):
    await ctx.bot.change_presence(activity=discord.Activity(
      type=discord.ActivityType.listening, name=status))

    await ctx.send(embed=discord.Embed(
      description=
      "<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully Changed the bot's presence to Listening",
      color=0x2f3136))

  @commands.is_owner()
  @commands.command(help="Change the bot's status")
  async def streaming(self, ctx: commands.Context, *, status: str):
    await ctx.bot.change_presence(
      activity=discord.Activity(type=discord.ActivityType.streaming,
                                name=status,
                                url="https://www.twitch.tv/#"))

    await ctx.send(embed=discord.Embed(
      description=
      "<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully Changed the bot's presence to Streaming.",
      color=0x2f3136))

  @commands.is_owner()
  @commands.command(help="Change the bot's status")
  async def watching(self, ctx: commands.Context, *, status: str):
    await ctx.bot.change_presence(activity=discord.Activity(
      type=discord.ActivityType.watching, name=status))

    await ctx.send(embed=discord.Embed(
      description=
      "<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully Changed the bot's presence to Watching.",
      color=0x2f3136))

  @commands.is_owner()
  @commands.command(help="Change the bot's status")
  async def playing(self, ctx: commands.Context, *, status: str):
    await ctx.bot.change_presence(
      activity=discord.Activity(type=discord.ActivityType.playing, name=status)
    )

    await ctx.send(embed=discord.Embed(
      description=
      "<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully Changed the bot's presence to Playing.",
      color=0x2f3136))

  @commands.is_owner()
  @commands.command(help="Change the bot's status")
  async def competing(self, ctx: commands.Context, *, status: str):
    await ctx.bot.change_presence(activity=discord.Activity(
      type=discord.ActivityType.competing, name=status))

    await ctx.send(embed=discord.Embed(
      description=
      "<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully Changed the bot's presence to Competing.",
      color=0x2f3136))

  @commands.group(name="apre", help="Allows you to add user in premium list)")
  @commands.is_owner()
  async def _apre(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(ctx.command)

  @_apre.command(name="list")
  @commands.is_owner()
  async def apre_list(self, ctx):
    with open("info.json") as f:
      apre = json.load(f)
      aprelist = apre["apre"]
      aprel = ([await self.client.fetch_user(nplu) for aprelu in aprelist])
      aprel = sorted(aprel, key=lambda nop: nop.created_at)
      entries = [
        f"`[{no}]` | [{mem}](https://discord.com/users/{mem.id}) (ID: {mem.id})"
        for no, mem in enumerate(npl, start=1)
      ]
      paginator = Paginator(source=DescriptionEmbedPaginator(
        entries=entries,
        title=f"Premium list of Titanium - {len(aprelist)}",
        description="",
        per_page=10,
        color=0x2f3136),
                            ctx=ctx)
      await paginator.paginate()

  @_apre.command(name="add", help="Add user to my premium list")
  @commands.is_owner()
  async def apre_add(self, ctx, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    apre = data["apre"]
    if user.id in apre:
      embed = discord.Embed(
        description=f"**The mentioned user is already in my premium list**",
        color=0x2f3136)
      await ctx.reply(embed=embed)
      return
    else:
      data["apre"].append(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      embed3110 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | Added {user} to the premium list",
        color=0x2f3136)

      await ctx.reply(embed=embed3110)

  @_apre.command(name="remove", help="Remove user from premium list")
  @commands.is_owner()
  async def apre_remove(self, ctx, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    apre = data["apre"]
    if user.id not in apre:
      embed = discord.Embed(
        description="**{} is not in premium list**".format(user),
        color=0x2f3136)
      await ctx.reply(embed=embed)
      return
    else:
      data["apre"].remove(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      embed1310 = discord.Embed(
        description=
        f"<a:tick_vaibhavs_lithium:1166037808868237364> | Removed {user} from premium list",
        color=0x2f3136)

      await ctx.reply(embed=embed1310)

  @commands.is_owner()
  @commands.command()
  async def leaveguild(self, ctx, guild: discord.Guild = None):

    #try:
    if guild is None:
      await ctx.send(embed=discord.Embed(
        description=
        "<a:botcross_vaibhavs_lithium:1084877519871823972> | Please provide me a server id",
        color=0x2f3136))
    else:
      await ctx.send(embed=discord.Embed(
        description=
        "<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully Left The Guild.",
        color=0x2f3136))
      await guild.leave()
