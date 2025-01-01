import discord
from discord.ext import commands
from difflib import get_close_matches
from contextlib import suppress
from core import Context
from core.Ventura import Ventura
from core.Cog import Cog
from utils.Tools import getConfig
from itertools import chain
from utils import *
import json
from utils import help as vhelp
from utils import Paginator, DescriptionEmbedPaginator, FieldPagePaginator, TextPaginator

client = Ventura()


class HelpView(discord.ui.Select):
  def __init__(self):
    
    opts = [discord.SelectOption(label="Antinuke", emoji="<a:antinuke:1198682146584404048>", description="Shows You Antinuke Commands"),
           discord.SelectOption(label="General", emoji="<:botantinuke_vaibhavs_lithium:1084877441920675920>", description="Shows You General Commands"),
           discord.SelectOption(label="Music", emoji="<:botvoice_vaibhavs_lithium:1086460797837914163>", description="Shows You Music Commands"),       
           discord.SelectOption(label="Moderation", emoji="<:botmod_vaibhavs_lithium:1084878106189373480>", description="Shows You Moderation Commands"), 
           discord.SelectOption(label="Welcome", emoji="<:welcomes_vaibhavs_lithium:1198649072844808242>", description="Shows You Welcome Commands"), 
           discord.SelectOption(label="VanityRoles", emoji="<a:vanity:1198657062956179566>", description="Shows You VanityRoles Commands"), 
           discord.SelectOption(label="Ticket", emoji="<:tickets:1205953531748552725>", description="Shows You Ticket Commands"),
           discord.SelectOption(label="Owner", emoji="<:ownership:1192023643224539156>", description="Shows You Owner Commands"),
           discord.SelectOption(label="Raidmode", emoji="<:botautomod_vaibhavs_lithium:1086466405819494521>", description="Shows You Raidmode Commands"),
           discord.SelectOption(label="Server", emoji="<:botserver_vaibhavs_lithium:1084878253141004430>", description="Shows You Server Commands"),
           discord.SelectOption(label="Games", emoji="<:botgames_vaibhavs_lithium:1086460417020272781>", description="Shows You Games Commands"), 
           discord.SelectOption(label="Utility", emoji="<:botutility_vaibhavs_lithium:1086460622465671238>", description="Shows You Utility Commands"),                  discord.SelectOption(label="Voice", emoji="<:botvoice_vaibhavs_lithium:1086460797837914163>", description="Shows You Voice Commands"), 
           discord.SelectOption(label="Vcroles", emoji="<:botvoice_vaibhavs_lithium:1086460797837914163>", description="Shows You Vcroles Commands"), 
           discord.SelectOption(label="Nsfw", emoji="<:botnsfw_vaibhavs_lithium:1084878161227030689>", description="Shows You Nsfw Commands"),
           discord.SelectOption(label="Ignore", emoji="<:chat:1205955954378543165>", description="Shows You Ignore Commands"),
           discord.SelectOption(label="Encryption", emoji="<:botEncryption_vaibhavs_lithium:1086461460999315486>", description="Shows You Encryption Commands"),
           discord.SelectOption(label="Fun", emoji="<:botfun_vaibhavs_lithium:1084877600385667202>", description="Shows You Fun Commands"),
           discord.SelectOption(label="Media", emoji="<:SocialMedia:1205956834180210819>", description="Shows You Media Commands"), 
           discord.SelectOption(label="Jsk", emoji="<:botjsk:1205957321138765825>", description="Shows You Jsk Commands"),        
           discord.SelectOption(label="Leveling", emoji="<:leveling:1205957976481996850>", description="Shows You Leveling Commands"), 
           discord.SelectOption(label="Reaction Roles", emoji="<:user:1205959357859373076>", description="Shows You Reaction Roles Commands"), 
           discord.SelectOption(label="Pfps", emoji="<:pfp:1205959753252077598>", description="Shows You Pfps Commands"), 
           discord.SelectOption(label="Verification", emoji="<a:Tick:1205892309347205140>", description="Shows You Verification Commands"),
           

            
            
           ]
    super().__init__(placeholder="Please Select A Module From Here.", max_values=1, min_values=1, options=opts)



  
  async def callback(self, interaction: discord.Interaction):

      mod = interaction.client.get_cog("anti")
      embed_mod = discord.Embed(title="<a:antinuke:1198682146584404048> Antinuke Commands", description="**__AntiNuke__**\n`antinuke` , `antinuke enable` , `antinuke disable` , `antinuke show` , `antinuke punishment set` , `antinuke whitelist` , `antinuke whitelist add` , `antinuke whitelist remove` , `antinuke whitelist show` , `antinuke whitelist reset` , `antinuke channelclean` , `antinuke roleclean` , `antinuke whitelist role` , `antinuke recover`", color=0x2f3136)
      embed_mod.set_footer(
                    text= "Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Antinuke":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("general")
      embed_mod = discord.Embed(title="<:botantinuke_vaibhavs_lithium:1084877441920675920> General Commands", description="**__General__**\n`afk` , `avatar` , `banner` , `servericon` , `membercount` , `poll` , `hack` , `token` , `users` , `italicize` , `strike` , `quote` , `code` , `bold` , `censor` , `underline` , `gender` , `wizz` , `pikachu` , `shorten` , `urban` , `rickroll` , `hash` , `snipe` , `roleall`", color=0x2f3136)
      embed_mod.set_footer(
  text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "General":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("Music")
      embed_mod = discord.Embed(title="<:botvoice_vaibhavs_lithium:1086460797837914163> Music Commands", description="**__Music__**\n`play` , `connect` , `disconnect` , `stop` , `skip`   ,  `pause` ,  `resume` , `bassboost`  , `move` , `volume` , `nowplaying` , `shuffle` , `pull` , `queue` , `queue clear` , `seek` ", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security",
                    icon_url=       "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Music":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("Moderation")
      embed_mod = discord.Embed(title="<:botmod_vaibhavs_lithium:1084878106189373480> Moderation Commands", description="**__Moderation__**\n`softban` , `purge` , `purge contains` , `purge startswith` , `purge invites` , `purge user` , `mute` , `unmute` , `kick` , `warn` , `ban` , `unban` , `clone` , `nick` , `slowmode` ,  `unslowmode` , `clear` , `clear all` , `clear bots` , `clear embeds` , `clear files` , `clear mentions` , `clear images` , `clear contains` , `clear reactions` , `nuke` , `lock` , `unlock` , `hide` , `unhide` , `hideall` , `unhideall` , `audit` , `sticker` , `emojisearch` , `stickersearch` , `role` , `role temp` , `role remove` , `role delete` , `role create` , `role rename` , `roleallhumans` , `roleallbots` , `removeallhumans` , `removeallbots`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Moderation":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("Welcome")
      embed_mod = discord.Embed(title="<:welcomes_vaibhavs_lithium:1198649072844808242> Welcome Commands", description="**__Fun__**\n` autorole bots add` , `autorole bots remove` , `autorole bots` , `autorole config` , `autorole humans add` , `autorole humans remove` , `autorole humans` , `autorole reset all` , `autorole reset bots` , `autorole reset humans` , `autorole reset` , `autorole`, `greet autodel` , `greet channel add` , `greet channel remove`, `greet channel` , `greet embed` , `greet image` , `greet message` , `greet ping` , `greet test` , `greet thumbnail` , `greet`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Welcome":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("vanityroles")
      embed_mod = discord.Embed(title="<a:vanity:1198657062956179566> Vanityroles Commands", description="**__Vanityroles__**\n`vanityroles` , `vanityroles show` , `vanityroles config` , `vanityroles reset` , `vanityroles setup`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Vanityroles":
        await interaction.response.edit_message(embed=embed_mod)


      mod = interaction.client.get_cog("Ticket")
      embed_mod = discord.Embed(title="<:tickets:1205953531748552725> Ticket Commands", description="**__Ticket__**\n`sendpanel`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Ticket":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("owner")
      embed_mod = discord.Embed(title="<:ownership:1192023643224539156> Owner Commands", description="**__Owner__**\n`eval` , `slist` , `restart` , `sync` , `np` , `np add` , `np remove` , `np list` , `bl show` , `bl add` , `bl remove` , `bdg` , `bdg add` , `bdg remove` , `dm` , `nick` , `globalban`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Owner":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("raidmode")
      embed_mod = discord.Embed(title="<:botautomod_vaibhavs_lithium:1086466405819494521> Raidmode Commands", description="**__Raidmode__**\n`automod` , `antispam on` , `antispam off` , `antilink off` ,  `antilink on`**", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Raidmode":
        await interaction.response.edit_message(embed=embed_mod)

    
      mod = interaction.client.get_cog("role")
      embed_mod = discord.Embed(title="<:botserver_vaibhavs_lithium:1084878253141004430> Server Commands", description="**__Server__**\n`setup` , `setup staff` , `setup girl` , `setup friend` , `setup vip` , `setup guest` , `setup owner` , `setup coowner` , `setup headadmin` , `setup admin` , `setup girladmin` , `setup headmod` , `setup mod` , `setup girlmod` , `setup config` , `staff` , `girl` , `friend` , `vip` , `guest` , `owner` , `coowner` , `headadmin` , `admin` , `girladmin ` , `headmod` , `mod` , `girlmod` , `remove staff` , `remove girl` , `remove friend` , `remove vip` , `remove guest` , `remove owner` , `remove coowner` , `remove headadmin` , `remove admin` , `remove girladmin` , `remove headmod` , `remove mod` , `remove girlmod` , `ar` , `ar create` , `ar delete` , `ar edit` , `ar config` **", color=0x2f3136)
      embed_mod.set_footer(
                    text="Made By Titanium Team",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Server":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("games")
      mbed_mod=discord.Embed(title = "<:botgames_vaibhavs_lithium:1086460417020272781> Games Commands", description="**__Games__**\n`akinator` , `chess` , `hangman` , `typerace` , `rps` , `reaction` , `tick-tack-toe` , `wordle` , `2048` , `memory-game` , `number-slider` , `battleship` , `country-guesser` **", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Games":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("extra")
      embed_mod = discord.Embed(title="<:botutility_vaibhavs_lithium:1086460622465671238> Utility Commands", description="**__Utility__**\n`stats` , `invite` , `serverinfo` , `userinfo` , `roleinfo` , `botinfo` , `status` , `emoji` , `user` , `role` , `channel` , `boosts`, `emoji-add` , `removeemoji` , `unbanall` ,  `joined-at` , `ping` , `github` , `vcinfo` , `channelinfo` , `note` , `notes` , `trashnotes` , `badges` , `ignore` , `ignore channel` , `ignore channel add` , `ignore channel remove` , `banner user` , `banner server` **", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Utility":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("voice")
      embed_mod = discord.Embed(title="<:botvoice_vaibhavs_lithium:1086460797837914163>Voice Commands", description="**__Voice__**\n`voice` , `voice kick` , `voice kickall` , `voice mute` , `voice muteall` , `voice unmute` , `voice unmuteall` , `voice deafen` , `voice deafenall` , `voice undeafen` , `voice undeafenall` , `voice moveall`**", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Voice":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("vcroles")
      embed_mod = discord.Embed(title="<:botvoice_vaibhavs_lithium:1086460797837914163>Vcroles Commands", description="**__Vcroles__**\n`vcrole bots add` , `vcrole bots remove` , `vcrole bots` , `vcrole config` , `vcrole humans add` , `vcrole humans remove` , `vcrole humans` , `vcrole reset` , `vcrole`**", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Vcroles":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("nsfw")
      embed_mod = discord.Embed(title="<:botnsfw_vaibhavs_lithium:1084878161227030689>Nsfw Commands", description="`nsfw` , `nsfw 4k` , `nsfw pussy` , `nsfw boobs` , `nsfw lewd` , `nsfw lesbian` , `nsfw blowjob` , `nsfw cum` , `nsfw gasm` , `nsfw hentai`**", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Nsfw":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("ignore")
      embed_mod = discord.Embed(title="<:chat:1205955954378543165>Ignore Commands", description="**__Ignore__**\n`ignore` , `ignore channel add` , `ignore channel remove`**", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Ignore":
        await interaction.response.edit_message(embed=embed_mod)
      
      mod = interaction.client.get_cog("encryption")
      embed_mod = discord.Embed(title="<:botEncryption_vaibhavs_lithium:1086461460999315486> Encryption Commands", description="**__Encryption__**\n`h encode` , `encode base85` , `encode ascii85` ,`encode base64` , `encode rot13` , `encode base32` , `encode hex` , `h decode` , `decode base85` , `decode base64` , `decode hex` , `decode ascii85` , `decode base32` , `decode rot13`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Encryption":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("fun")
      embed_mod = discord.Embed(title="<:botfun_vaibhavs_lithium:1084877600385667202> Fun Commands", description="**__Fun__**\n` tickle` , `kiss` , `hug` , `slap` , `pat` , `feed` , `pet` , `howgay` , `slots` , ` penis` , `meme` , `cat` , `iplookup`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Fun":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("media")
      embed_mod = discord.Embed(title="<:SocialMedia:1205956834180210819> Media Commands", description="**__Media__**\n`media` , `media setup <channel>` , `media remove <channel>`, `media config`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Media":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("jsk")
      embed_mod = discord.Embed(title="<:botjsk:1205957321138765825> Jsk Commands", description="**__Jsk__**\n`jsk` , `jsk rtt` , `jsk curl` z `jsk debug` , `jsk sync` , `jsk py`  , `jsk permtrace` , `jsk retain` , `jsk tasks` , `jsk timeit` , `jsk dis` , `jsk sql` , `jsk py_inspect` , `jsk hide` , `jsk voice` , `jsk git` , `jsk show` , `jsk cancel` , `jsk shell` , `jsk load` , `jsk unload` , `jsk override` , `jsk invite` , `jsk shutdown` , `jsk pip` , `jsk repeat`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Jsk":
        await interaction.response.edit_message(embed=embed_mod)

      mod = interaction.client.get_cog("leveling")
      embed_mod = discord.Embed(title="<:leveling:1205957976481996850> Leveling Commands", description="**__Leveling__**\n`leveling enable` , `leveling channel <channel>` , `xp`, `leaderboard/lb`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Leveling":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("reactionroles")
      embed_mod = discord.Embed(title= "<:user:1205959357859373076> Reaction Roles Commands", description="**__Reaction Roles__**\n`reaction <emote> <role> <channel> [title=None]`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Reaction Roles":
        await interaction.response.edit_message(embed=embed_mod)
      mod = interaction.client.get_cog("pfps")
      embed_mod = discord.Embed(title="<:pfp:1205959753252077598> Pfps Commands", description="**__Pfps__**\n`pic`, `boys` , `girls`, `couples`, `anime`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Pfps":
        await interaction.response.edit_message(embed=embed_mod)


      mod = interaction.client.get_cog("verification")
      embed_mod = discord.Embed(title="<a:Tick:1205892309347205140> Verification Commands", description="**__Verification__**\n`verification enable` , `verification disable` , `verification config`", color=0x2f3136)
      embed_mod.set_footer(
                    text="Thanks For Choosing Titanium Security!",
                    icon_url=
                    "https://discord.com/channels/@me/1108702152748175373/1118195215019282542"
                )
      if self.values[0] == "Verification":
        await interaction.response.edit_message(embed=embed_mod)  
      

      

      













class dropdown(discord.ui.View):
  def __init__(self, *, timeout=None):
     super().__init__(timeout=timeout)
     self.add_item(HelpView())
     self.response = None














      




















      

    
class HelpCommand(commands.HelpCommand):

    async def on_help_command_error(self, ctx, error):
        damn = [
            commands.CommandOnCooldown, commands.CommandNotFound,
            discord.HTTPException, commands.CommandInvokeError
        ]
        if not type(error) in damn:
            await self.context.reply(
                f"Unknown Error Occurred\n{error.original}",
                mention_author=False)
        else:
            if type(error) == commands.CommandOnCooldown:
                return

                return await super().on_help_command_error(ctx, error)

  
    async def command_not_found(self, string: str) -> None:
        with open('blacklist.json', 'r') as f:
            data = json.load(f)
        if str(self.context.author.id) in data["ids"]:
            embed = discord.Embed(
                title="<a:botcross_vaibhavs_lithium:1084877519871823972> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.com/invite/MnPsa4ZFJ3)",
                color=0x2f3136)
            await self.context.reply(embed=embed, mention_author=False)
        else:

            if string in ("security", "anti","antinuke"):
                cog = self.context.bot.get_cog("Antinuke")
                with suppress(discord.HTTPException):
                    await self.send_cog_help(cog)
            else:
                msg = f"Command `{string}` is not found...\n"
                gulzaib = await self.context.bot.fetch_user(1035963644879569027)
                cmds = (str(cmd) for cmd in self.context.bot.walk_commands())
                mtchs = get_close_matches(string, cmds)
                if mtchs:
                    for okaay, okay in enumerate(mtchs, start=1):
                        msg += f"Did You Mean: \n`[{okaay}]`. `{okay}`\n"
                embed1 = discord.Embed(
                    color=0x2f3136,
                    title=f"Command `{string}` is not found...\n",
                    description=f"Did You Mean: \n`[{okaay}]`. `{okay}`\n")
                embed1.set_footer(text=f"Developed By {gulzaib}",
                                  icon_url=gulzaib.display_avatar.url)
                return None

    async def send_bot_help(self, mapping):
        await self.context.typing()
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        with open('blacklist.json', 'r') as f:
            bled = json.load(f)
        if str(self.context.author.id) in bled["ids"]:
            embed = discord.Embed(
                title="<a:botcross_vaibhavs_lithium:1084877519871823972> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.com/invite/MnPsa4ZFJ3)",
                color=0x2f3136)
            return await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        data = getConfig(self.context.guild.id)
        prefix = data["prefix"]
        perms = discord.Permissions.none()
        perms.read_messages = True
        perms.external_emojis = True
        perms.send_messages = True
        perms.manage_roles = True
        perms.manage_channels = True
        perms.ban_members = True
        perms.kick_members = True
        perms.manage_messages = True
        perms.embed_links = True
        perms.read_message_history = True
        perms.attach_files = True
        perms.add_reactions = True
        perms.administrator = True
        inv = discord.utils.oauth_url(self.context.bot.user.id,
                                      permissions=perms)
        filtered = await self.filter_commands(self.context.bot.walk_commands(),
                                              sort=True)
        
        embed = discord.Embed(
            title="Titanium Security | Help Menu",
            description=
            f"<a:arrow_arrow_vaibhavs_lithium:1094495285780152461> **Titanium Prefix** Is `{prefix}` \n<a:arrow_arrow_vaibhavs_lithium:1094495285780152461> Total Commands:** {len(set(self.context.bot.walk_commands()))} **| Usable by you (here):** {len(set(filtered))}**\n<a:arrow_arrow_vaibhavs_lithium:1094495285780152461> Type `{prefix}`help <command | module>` for more info.\n<a:arrow_arrow_vaibhavs_lithium:1094495285780152461> **Join My [Support](https://discord.com/invite/MnPsa4ZFJ3)**",
            color=0x2f3136)
        embed.set_thumbnail(url=self.context.bot.user.display_avatar.url)
         
        embed.add_field(
        name="__Main Modules__",
            value=
            """<a:antinuke:1198682146584404048> AntiNuke\n<:botantinuke_vaibhavs_lithium:1084877441920675920> General\n<:botvoice_vaibhavs_lithium:1086460797837914163> Music\n<:botmod_vaibhavs_lithium:1084878106189373480> Moderation\n<:welcomes_vaibhavs_lithium:1198649072844808242> Welcome\n<a:vanity:1198657062956179566> Vanityroles\n<:tickets:1205953531748552725> Ticket\n<:ownership:1192023643224539156> Owner""",
            inline=True)
        embed.add_field(
            name="__Advance Modules__",
            value=
            """<:botautomod_vaibhavs_lithium:1086466405819494521> Raidmode\n<:botserver_vaibhavs_lithium:1084878253141004430> Server\n<:botgames_vaibhavs_lithium:1086460417020272781> Games\n<:botutility_vaibhavs_lithium:1086460622465671238> Utility\n<:botvoice_vaibhavs_lithium:1086460797837914163> Voice\n<:botvoice_vaibhavs_lithium:1086460797837914163> VcRoles\n<:botnsfw_vaibhavs_lithium:1084878161227030689> Nsfw\n<:chat:1205955954378543165> Ignore""",
            inline=True)
        embed.add_field(
            name="__Extra Modules__",
            value=
            """<:botEncryption_vaibhavs_lithium:1086461460999315486> Encryption\n<:botfun_vaibhavs_lithium:1084877600385667202> Fun\n<:SocialMedia:1205956834180210819> Media\n<:botjsk:1205957321138765825> Jsk\n<:leveling:1205957976481996850> Leveling\n<:user:1205959357859373076> Reaction Roles\n<:pfp:1205959753252077598> Pfp\n<a:Tick:1205892309347205140> Verification""",
            inline=True)
        embed.set_author(name=self.context.author.name,
                         icon_url=self.context.author.display_avatar.url)    
      

        view = vhelp.View(mapping = mapping, ctx = self.context, homeembed = embed, ui = 2).add_item(HelpView())
        await self.context.reply(embed=embed, mention_author=False, view=view)

    async def send_command_help(self, command):
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        with open('blacklist.json', 'r') as f:
            data = json.load(f)
        if str(self.context.author.id) in data["ids"]:
            embed = discord.Embed(
                title="<a:botcross_vaibhavs_lithium:1084877519871823972> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.com/invite/MnPsa4ZFJ3)",
                color=0x2f3136)
            await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        else:
            hacker = f">>> {command.help}" if command.help else '>>> No Help Provided...'
            embed = discord.Embed(
                description=
                f"""```yaml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Commands !```\n{hacker}""",
                color=0x2f3136)
            alias = ' | '.join(command.aliases)

            embed.add_field(
                name="**Aliases**",
                value=f"{alias}" if command.aliases else "No Aliases",
                inline=False)
            embed.add_field(
                name="**Usage**",
                value=f"`{self.context.prefix}{command.signature}`\n")
            embed.set_author(name=f"{command.cog.qualified_name.title()}",
                             icon_url=self.context.bot.user.display_avatar.url)
            await self.context.reply(embed=embed, mention_author=False)

    def get_command_signature(self, command: commands.Command) -> str:
        parent = command.full_parent_name
        if len(command.aliases) > 0:
            aliases = ' | '.join(command.aliases)
            fmt = f'[{command.name} | {aliases}]'
            if parent:
                fmt = f'{parent}'
            alias = f'[{command.name} | {aliases}]'
        else:
            alias = command.name if not parent else f'{parent} {command.name}'
        return f'{alias} {command.signature}'

    def common_command_formatting(self, embed_like, command):
        embed_like.title = self.get_command_signature(command)
        if command.description:
            embed_like.description = f'{command.description}\n\n{command.help}'
        else:
            embed_like.description = command.help or 'No help found...'


    async def send_group_help(self, group):
        with open('blacklist.json', 'r') as f:
            idk = json.load(f)
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        if str(self.context.author.id) in idk["ids"]:
            embed = discord.Embed(
                title="<a:botcross_vaibhavs_lithium:1084877519871823972> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.com/invite/MnPsa4ZFJ3)",
                color=0x2f3136)
            await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        else:
            entries = [(
            f"`{self.context.prefix}{cmd.qualified_name}`",
            f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
        ) for cmd in group.commands]
        paginator = Paginator(source=FieldPagePaginator(
            entries=entries,
            title=f"{group.qualified_name} Commands",
            description="<...> Duty | [...] Optional\n\n",
            color=0x2f3136,
            per_page=10),
                              ctx=self.context)
        await paginator.paginate()

        
    
    async def send_cog_help(self, cog):
        with open('blacklist.json', 'r') as f:
            data = json.load(f)
        with open('ignore.json', 'r') as heck:
            randi = json.load(heck)
        if str(self.context.author.id) in data["ids"]:
            embed = discord.Embed(
                title="<a:botcross_vaibhavs_lithium:1084877519871823972> Blacklisted",
                description=
                "You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.com/invite/MnPsa4ZFJ3)",
                color=0x2f3136)
            return await self.context.reply(embed=embed, mention_author=False)
        elif str(self.context.channel.id) in randi["ids"]:
            return None
        #await self.context.typing()
        entries = [(
            f"`{self.context.prefix}{cmd.qualified_name}`",
            f"{cmd.short_doc if cmd.short_doc else 'No Description Provided...'}\n\n"
        ) for cmd in cog.get_commands()]
        paginator = Paginator(source=FieldPagePaginator(
            entries=entries,
            title=f"{cog.qualified_name.title()} ({len(cog.get_commands())})",
            description="<...> Duty | [...] Optional\n\n",
            color=0x2f3136,
            per_page=10),
                              ctx=self.context)
        await paginator.paginate()


class Help(Cog, name="help"):

    def __init__(self, client: Ventura):
        self._original_help_command = client.help_command
        attributes = {
            'name':
            "help",
            'aliases': ['h'],
            'cooldown':
            commands.CooldownMapping.from_cooldown(1, 5,
                                                   commands.BucketType.user),
            'help':
            'Shows help about bot, a command or a category'
        }
        client.help_command = HelpCommand(command_attrs=attributes)
        client.help_command.cog = self

    async def cog_unload(self):
        self.help_command = self._original_help_command




"[Invite]({inv}) | [Support](https://discord.com/invite/MnPsa4ZFJ3)",