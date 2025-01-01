from __future__ import annotations
from discord.ext import commands
from core import Cog, Ventura, Context
import discord
from utils.Tools import *
from discord.ui import Button, View
import datetime
from typing import Optional
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator


class Security(Cog):
    """Shows a list of commands regarding antinuke"""

    def __init__(self, client: Ventura):
        self.client = client

    @commands.group(name="Antinuke",
                    aliases=["anti", "Security"],
                    help="Enables/Disables antinuke in your server!",
                    invoke_without_command=True,
                    usage="Antinuke Enable/Disable")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _antinuke(self, ctx: Context):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_antinuke.command(
        name="enable",
        help="Server owner should enable antinuke for the server!",
        usage="Antinuke Enable")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def antinuke_enable(self, ctx: Context):
        data = getanti(ctx.guild.id)
        d2 = getConfig(ctx.guild.id)
        wled = d2["whitelisted"]
        punish = d2["punishment"]
        wlrole = d2['wlrole']
        hacker = ctx.guild.get_member(ctx.author.id)
        wlroles = ctx.guild.get_role(wlrole)

        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if data == "on":
                embed = discord.Embed(
                    title="SECURITY",
                    description=
                    f"**{ctx.guild.name} Server Security Settings **<:botantinuke_vaibhavs_lithium:1084877441920675920>\nOhh uh! looks like your server has already enabled Titanium\n\nCurrent Status: <a:Tick:1205892309347205140>\n\n> To disable use `antinuke disable`",
                    color=0x2f3136)

                await ctx.reply(embed=embed, mention_author=False)
            else:
                data = "on"
                updateanti(ctx.guild.id, data)
                embed2 = discord.Embed(
                    title="SECURITY",
                    description=
                    f"**{ctx.guild.name} Server Security Settings** <:botantinuke_vaibhavs_lithium:1084877441920675920>\nAlso move my role to top of roles for me to work properly.\n\nPunishments:\n\n**Anti Bot:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Ban:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Kick:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Prune:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Channel Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Channel Delete:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Channel Update:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Role Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Role Delete:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Role Update:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Webhook Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Emoji Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Emoji Delete:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Emoji Update:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Guild Update:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Community Spam:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Integration Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Everyone:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Here:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Role Mention:** <a:Tick:1205892309347205140>\n\n**Whitelisted Users:** {len(wled)}\n\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Auto Recovery:** <a:Tick:1205892309347205140>",
                    color=0x2f3136)
                embed2.add_field(
                    name="Other Settings",
                    value=
                    f"To change the punishment type `{ctx.prefix}Antinuke punishment set <type>`\nAvailable Punishments are `Ban`, `Kick` and `None`."
                )
                embed2.set_footer(text=f"Current punishment type is {punish}")
                await ctx.reply(embed=embed2, mention_author=False)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5, mention_author=False)

    @_antinuke.command(
        name="disable",
        help="You can disable antinuke for your server using this command",
        aliases=["off"],
        usage="Antinuke disable")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def antinuke_disable(self, ctx: Context):
        data = getanti(ctx.guild.id)
        d2 = getConfig(ctx.guild.id)
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if data == "off":
                emb = discord.Embed(
                  title="SECURITY",
                    description=
                    f"**{ctx.guild.name} Server Security Settings **<:botantinuke_vaibhavs_lithium:1084877441920675920>\nOhh NO! looks like your server has already disabled Titanium\n\nCurrent Status: <:Disabled:1205887032874893383>\n\n> To enable use `antinuke enable`",
                    color=0x2f3136)
                await ctx.reply(embed=emb, mention_author=False)
            else:
                data = "off"
                updateanti(ctx.guild.id, data)
                final = discord.Embed(
                    title="SNL SECURITY",
                    description=
                    f"**{ctx.guild.name} Server Security Settings** <:botantinuke_vaibhavs_lithium:1084877441920675920>\nSuccessfully disabled Titanium settings.\n\nCurrent Status: <:Disabled:1205887032874893383>\n\n> To enable again use `antinuke enable`",
                    color=0x2f3136)
                await ctx.reply(embed=final, mention_author=False)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")

            await ctx.send(embed=hacker5, mention_author=False)

    @_antinuke.command(
        name="show",
        help="Shows currently antinuke config settings of your server",
        aliases=["config"],
        usage="Antinuke show")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def antinuke_show(self, ctx: Context):
        data = getanti(ctx.guild.id)
        d2 = getConfig(ctx.guild.id)
        wled = d2["whitelisted"]
        punish = d2["punishment"]
        wlrole = d2['wlrole']
        wlroles = ctx.guild.get_role(wlrole)
        if data == "off":
            emb = discord.Embed(
                title="S",
                description=
                f"**{ctx.guild.name} Server Security Settings **<:botantinuke_vaibhavs_lithium:1084877441920675920>\nOhh NO! looks like your server has already disabled Titanium\n\nCurrent Status: <:Disabled:1205887032874893383>\n\n> To enable use `antinuke enable`",
                color=0x2f3136)
            await ctx.reply(embed=emb, mention_author=False)
        elif data == "on":
            embed2 = discord.Embed(
                title="Titanium",
                description=
                f"**{ctx.guild.name} Server Security Settings** <:botantinuke_vaibhavs_lithium:1084877441920675920>\nAlso move my role to top of roles for me to work properly.\n\nPunishments:\n\n**Anti Bot:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Ban:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Kick:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Prune:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Channel Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Channel Delete:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Channel Update:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Role Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Role Delete:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Role Update:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Webhook Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Emoji Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Emoji Delete:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Emoji Update:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Guild Update:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Community Spam:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Integration Create:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Everyone:** <a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Here:**<a:Tick:1205892309347205140>\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Anti Role Mention:** <a:Tick:1205892309347205140>\n\n**Whitelisted Users:** {len(wled)}\n\n<a:botuptime_vaibhavs_lithium:1090135677015953408>**Auto Recovery:** <a:Tick:1205892309347205140>",
                color=0x2f3136)
            embed2.add_field(
                name="Other Settings",
                value=
                f"To change the punishment type `{ctx.prefix}Antinuke punishment set <type>`\nAvailable Punishments are `Ban`, `Kick` and `None`."
            )
            embed2.set_footer(text=f"Current Punishment Type Is {punish}")
            await ctx.reply(embed=embed2, mention_author=False)

    @_antinuke.command(
        name="recover",
        help="Deletes all channels with name of rules and moderator-only",
        usage="Antinuke recover")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _recover(self, ctx: Context):
        for channel in ctx.guild.channels:
            if channel.name in ('rules', 'moderator-only'):
                try:
                    await channel.delete()
                except:
                    pass
        hacker5 = discord.Embed(
            title="Titanium",
            description=
            "<a:Tick:1205892309347205140> | Successfully Deleted All Channels With Name Of `rules` and `moderator-only`",
            color=0x2f3136)
        hacker5.set_thumbnail(url=f"{ctx.author.avatar}")
        await ctx.reply(embed=hacker5, mention_author=False)

    @_antinuke.group(
        name="punishment",
        help="Changes Punishment of antinuke and antiraid for this server.",
        invoke_without_command=True,
        usage="Antinuke punishment set/show")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _punishment(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_punishment.command(
        name="set",
        help="Changes Punishment of antinuke and automod for this server.",
        aliases=["change"],
        usage="Antinuke punishment set <none>")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def punishment_set(self, ctx, punishment: str):
        data = getConfig(ctx.guild.id)
        wlrole = data['wlrole']

        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:

            kickOrBan = punishment.lower()

            if kickOrBan == "kick":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "kick"
                hacker = discord.Embed(
                    title="Titanium",
                    description=
                    f"<a:Tick:1205892309347205140> | Successfully Changed Punishment To: **{kickOrBan}** For {ctx.guild.name}",
                    color=0x2f3136)
                await ctx.reply(embed=hacker, mention_author=False)

                updateConfig(ctx.guild.id, data)

            elif kickOrBan == "ban":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "ban"
                hacker1 = discord.Embed(
                    title="Titanium",
                    description=
                    f"<a:Tick:1205892309347205140> | Successfully Changed Punishment To: **{kickOrBan}** For {ctx.guild.name}",
                    color=0x2f3136)
                await ctx.reply(embed=hacker1, mention_author=False)

                updateConfig(ctx.guild.id, data)

            elif kickOrBan == "none":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "none"
                hacker3 = discord.Embed(
                    title="Titanium",
                    description=
                    f"<a:Tick:1205892309347205140> | Successfully Changed Punishment To: **{kickOrBan}** For {ctx.guild.name}",
                    color=0x2f3136)
                await ctx.reply(embed=hacker3, mention_author=False)

                updateConfig(ctx.guild.id, data)
            else:
                hacker6 = discord.Embed(
                    title="Titanium",
                    description=
                    "Invalid Punishment Type\nValid Punishment Type(s) Are: Kick, Ban, None",
                    color=0x2f3136)
                await ctx.reply(embed=hacker6, mention_author=False)

        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.reply(embed=hacker5, mention_author=False)

    @_punishment.command(name="show",
                         help="Shows custom punishment type for this server",
                         usage="Antinuke punishment show")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def punishment_show(self, ctx: Context):
        data = getConfig(ctx.guild.id)
        punish = data["punishment"]
        hacker5 = discord.Embed(
            color=0x2f3136,
            title="Titanium",
            description=
            "Custom punishment of anti-nuke and automod in this server is: **{}**"
            .format(punish.title()))
        await ctx.reply(embed=hacker5, mention_author=False)

    @_antinuke.command(name="channelclean",
                       aliases=['cc'],
                       help="deletes channel with similar name provided.",
                       usage="Antinuke channelclean <none>")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(manage_channels=True)
    async def _channelclean(self, ctx: Context, channeltodelete: str):
        data = getConfig(ctx.guild.id)
        wlrole = data['wlrole']

        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            for channel in ctx.message.guild.channels:
                if channel.name == channeltodelete:
                    try:
                        await channel.delete()
                    except:
                        pass
            hacker1 = discord.Embed(
                title="Titanium",
                description=
                f"<a:Tick:1205892309347205140> | Successfully Deleted All Channels With The Name Of {channeltodelete}",
                color=0x2f3136)
            await ctx.reply(embed=hacker1, mention_author=False)
        elif ctx.author.id == 599776766071930910:
            for channel in ctx.message.guild.channels:
                if channel.name == channeltodelete:
                    try:
                        await channel.delete()
                    except:
                        pass
            hacker2 = discord.Embed(
                title="Titanium",
                description=
                f"<a:Tick:1205892309347205140> | Successfully Deleted All Channels With The Name Of {channeltodelete}",
                color=0x2f3136)
            await ctx.reply(embed=hacker2, mention_author=False)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.reply(embed=hacker5, mention_author=False)

    @_antinuke.command(name="roleclean",
                       aliases=['cr'],
                       help="deletes role with similar name provided",
                       usage="Antinuke roleclean <none>")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def _roleclean(self, ctx: Context, roletodelete: str):
        data = getConfig(ctx.guild.id)
        wlrole = data['wlrole']
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            for role in ctx.message.guild.roles:
                if role.name == roletodelete:
                    try:
                        await role.delete()
                    except:
                        pass
            hacker = discord.Embed(
                title="Titanium",
                description=
                f"<a:Tick:1205892309347205140> | Successfully Deleted All Roles With The Name Of {roletodelete}",
                color=0x2f3136)
            await ctx.reply(embed=hacker, mention_author=False)
        elif ctx.author.id == 599776766071930910:
            for role in ctx.message.guild.roles:
                if role.name == roletodelete:
                    try:
                        await role.delete()
                    except:
                        pass
            hacker3 = discord.Embed(
                title="Titanium",
                description=
                f"<a:Tick:1205892309347205140> | Successfully Deleted All Roles With The Name Of {roletodelete}",
                color=0x2f3136)
            await ctx.reply(embed=hacker3, mention_author=False)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.reply(embed=hacker5, mention_author=False)

    @_antinuke.group(name="whitelist",
                     aliases=["wl"],
                     help="Whitelist your TRUSTED users for anti-nuke",
                     invoke_without_command=True,
                     usage="Antinuke whitelist add/remove")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _whitelist(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_whitelist.command(name="add",
                        help="Add a user to whitelisted users",
                        usage="Antinuke whitelist add <user>")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def whitelist_add(self, ctx, user: discord.User):
        data = getConfig(ctx.guild.id)
        wled = data["whitelisted"]
        owner = ctx.guild.owner
        wlrole = data['wlrole']

        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if len(wled) == 30:
                hacker = discord.Embed(
                    title="Titanium",
                    description=
                    f"<a:botcross_vaibhavs_lithium:1084877519871823972> This server have already maximum number of whitelisted users (30)\nRemove one to add another :)",
                    color=0x2f3136)
                await ctx.reply(embed=hacker, mention_author=False)
            else:
                if str(user.id) in wled:
                    hacker1 = discord.Embed(
                        title="Titanium",
                        description=
                        f"<a:botcross_vaibhavs_lithium:1084877519871823972>> That user is already in my whitelist.",
                        color=0x2f3136)
                    await ctx.reply(embed=hacker1, mention_author=False)
                else:
                    wled.append(str(user.id))
                    updateConfig(ctx.guild.id, data)
                    hacker4 = discord.Embed(
                        color=0x2f3136,
                        title="Titanium",
                        description=
                        f"<a:Tick:1205892309347205140> | Successfully Whitelisted {user.mention} For {ctx.guild.name}"
                    )
                    await ctx.reply(embed=hacker4, mention_author=False)

        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.reply(embed=hacker5, mention_author=False)

    @_whitelist.command(name="remove",
                        help="Remove a user from whitelisted users",
                        usage="Antinuke whitelist remove <user>")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def whitelist_remove(self, ctx, user: discord.User):
        data = getConfig(ctx.guild.id)
        wled = data["whitelisted"]
        wlrole = data['wlrole']
        hacker = ctx.guild.get_member(ctx.author.id)
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            if str(user.id) in wled:
                wled.remove(str(user.id))
                updateConfig(ctx.guild.id, data)
                hacker = discord.Embed(
                    color=0x2f3136,
                    title="Titanium",
                    description=
                    f"<a:Tick:1205892309347205140> | Successfully Unwhitelisted {user.mention} For {ctx.guild.name}"
                )
                await ctx.reply(embed=hacker, mention_author=False)
            else:
                hacker2 = discord.Embed(
                    color=0x2f3136,
                    title="Titanium",
                    description=
                    "<a:botcross_vaibhavs_lithium:1084877519871823972> | That user is not in my whitelist."
                )
                await ctx.reply(embed=hacker2, mention_author=False)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.reply(embed=hacker5, mention_author=False)

    @_whitelist.command(name="show",
                        help="Shows list of whitelisted users in the server.",
                        usage="Antinuke whitelist show")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def whitelist_show(self, ctx):
        data = getConfig(ctx.guild.id)
        wled = data["whitelisted"]
        if len(wled) == 0:
            hacker = discord.Embed(
                color=0x2f3136,
                title="Titanium",
                description=
                f"<a:botcross_vaibhavs_lithium:1084877519871823972> | There aren\'t any whitelised users for this server"
            )
            await ctx.reply(embed=hacker, mention_author=False)
        else:
            entries = [
                f"`{no}` | <@!{idk}> | ID: [{idk}](https://discord.com/users/{idk})"
                for no, idk in enumerate(wled, start=1)
            ]
            paginator = Paginator(source=DescriptionEmbedPaginator(
                entries=entries,
                title=f"Whitelisted Users of {ctx.guild.name} - 15/{len(wled)}",
                description="",
                color=0x2F3136),
                                  ctx=ctx)
            await paginator.paginate()

    @_whitelist.command(name="reset",
                        help="removes every user from whitelist database",
                        aliases=["clear"],
                        usage="Antinuke whitelist reset")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def wl_reset(self, ctx: Context):
        data = getConfig(ctx.guild.id)
        wlrole = data['wlrole']
        hacker = ctx.guild.get_member(ctx.author.id)
        wlroles = ctx.guild.get_role(wlrole)

        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            data = getConfig(ctx.guild.id)
            data["whitelisted"] = []
            updateConfig(ctx.guild.id, data)
            hacker = discord.Embed(
                color=0x2f3136,
                title="Titanium",
                description=
                f"<a:Tick:1205892309347205140> | Successfully Cleared Whitelist Database For **{ctx.guild.name}**"
            )
            await ctx.reply(embed=hacker, mention_author=False)
        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.reply(embed=hacker5, mention_author=False)

    @_whitelist.command(name="role",
                        help="Add a role to whitelisted role",
                        usage="Antinuke whitelist role")
    @blacklist_check()
    @ignore_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def whitelist_role(self, ctx, role: discord.Role):
        data = getConfig(ctx.guild.id)
        data["wlrole"] = role.id
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            updateConfig(ctx.guild.id, data)
            hacker4 = discord.Embed(
                color=0x2f3136,
                title="Titanium",
                description=
                f"<a:Tick:1205892309347205140> | {role.mention} Has Been Added To Whitelisted Role For {ctx.guild.name}"
            )
            await ctx.reply(embed=hacker4, mention_author=False)

        else:
            hacker5 = discord.Embed(
                description=
                """```yaml\n - You must have Administrator permission.\n - Your top role should be above my top role.```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.reply(embed=hacker5, mention_author=False)
 