import discord
import json
import random
from discord.ext import commands
from core import *
from utils.Tools import *
from core.Ventura import Ventura

class Leveling(commands.Cog):
    def __init__(self, client):
        self.client = client
      
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
      with open('leveling.json', "r") as f:
        beta = json.load(f)
      if not str(guild.id) in beta:
        beta[str(guild.id)] = {"enabled": False}
      with open('leveling.json', "w") as f:
        json.dump(f,beta,indent=4)
      with open('data.json', 'r') as f:
        okbuddy = json.load(f)
      if not str(guild.id) in okbuddy:
        okbuddy[str(guild.id)] = {}
      with open('data.json', "w") as f:
        json.dump(f,okbuddy, indent=4)



    @commands.Cog.listener()
    async def on_ready(self):
      with open('leveling.json', "f") as f:
        beta = json.load(f)
      with open('data.json', 'f') as f:
        okbuddy = json.load(f)
      for guild in self.client.guilds:
        if not str(guild.id) in beta:
          beta[str(guild.id)] = {"enabled": False}
      with open('leveling.json', "w") as f:
        json.dump(beta, f, indent=4)
      for guild in self.client.guilds:
        print(guild.id)
        if not str(guild.id) in okbuddy:
          okbuddy[str(guild.id)] = {}
      with open('data.json', "w") as f:
        json.dump(okbuddy, f, indent=4)
  
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        with open("leveling.json", "r") as f:
            leveling = json.load(f)

        if str(message.guild.id) not in leveling:
            return

        if leveling[str(message.guild.id)]["enabled"] == False:
            return

        with open("data.json", "r") as f:
            data = json.load(f)

        if str(message.guild.id) not in data:
            data[str(message.guild.id)] = {}

            with open("data.json", "w") as f:
                json.dump(data, f, indent = 4)

        if str(message.author.id) not in data[str(message.guild.id)]:
            data[str(message.guild.id)][str(message.author.id)]["xp"] = 0
            data[str(message.guild.id)][str(message.author.id)]["level"] = 1

            with open("data.json", "w") as f:
                json.dump(data, f, indent = 4)
        else:
            data[str(message.guild.id)][str(message.author.id)]["xp"] += random.randint(1, 5)

            with open("data.json", "w") as f:
                json.dump(data, f, indent = 4)

            xp = data[str(message.guild.id)][str(message.author.id)]["xp"]
            lvl = data[str(message.guild.id)][str(message.author.id)]["level"]
            with open("levels.json", "r") as f:
                levels = json.load(f)

            nxt_lvl = levels[str(lvl)]["xp"]

            if xp >= nxt_lvl or xp == nxt_lvl:
                data[str(message.guild.id)][str(message.author.id)]["level"] += 1
                data[str(message.guild.id)][str(message.author.id)]["xp"] = 0

                with open("data.json", "w") as f:
                    json.dump(data, f, indent = 4)

                channel = self.client.get_channel(leveling[str(message.guild.id)]["channel"])

                await channel.send(f"{message.author.mention} has leveled up to level {lvl + 1}!")


    @commands.hybrid_group(name="leveling", invoke_without_command = True)
    async def leveling(self, ctx):
        print("skib")


    @leveling.command(name="enable", description="Enables leveling in your server")
    @commands.has_permissions(administrator = True)
    async def enable(self, ctx):
      #if not int(ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
       # return await ctx.send("<:icons_exclamation:1088092340519960636> | Your top role should be above my top role.")
        with open("data.json", "r") as f:
            data = json.load(f)

        if str(ctx.author.id) not in data[str(ctx.guild.id)]:
            data[str(ctx.guild.id)][str(ctx.author.id)] = {}
            data[str(ctx.guild.id)][str(ctx.author.id)]["xp"] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]["level"] = 1

            with open("data.json", "w") as f:
                json.dump(data, f, indent = 4)

        else:
            pass

        with open("leveling.json", "r") as f:
            leveling = json.load(f)

        if str(ctx.guild.id) not in leveling:
            leveling[str(ctx.guild.id)] = {}
            leveling[str(ctx.guild.id)]["enabled"] = True

            with open("leveling.json", "w") as f:
                json.dump(leveling, f, indent = 4)

            await ctx.send("<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully enabled leveling")

        else:
            leveling[str(ctx.guild.id)]["enabled"] = True

            with open("leveling.json", "w") as f:
                json.dump(leveling, f, indent = 4)

            await ctx.send("<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully enabled leveling")


    @leveling.command(name="disable", description="Disables leveling in your server")
    @commands.has_permissions(administrator = True)
    async def disable(self, ctx):
    #  if not int(ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
      #  return await ctx.send("<a:cross:1088298797467193344> | Your top role should be above my top role.")
        with open("data.json", "r") as f:
            data = json.load(f)

        if str(ctx.author.id) not in data[str(ctx.guild.id)]:
            data[str(ctx.guild.id)][str(ctx.author.id)] = {}
            data[str(ctx.guild.id)][str(ctx.author.id)]["xp"] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]["level"] = 1

            with open("data.json", "w") as f:
                json.dump(data, f, indent = 4)

        else:
            pass

        with open("leveling.json", "r") as f:
            leveling = json.load(f)

        if str(ctx.guild.id) not in leveling:
            leveling[str(ctx.guild.id)] = {}
            leveling[str(ctx.guild.id)]["enabled"] = False

            with open("leveling.json", "w") as f:
                json.dump(leveling, f, indent = 4)

            await ctx.send("<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully disabled leveling")

        else:
            leveling[str(ctx.guild.id)]["enabled"] = False

            with open("leveling.json", "w") as f:
                json.dump(leveling, f, indent = 4)

            await ctx.send("<a:tick_vaibhavs_lithium:1166037808868237364> | Successfully disabled leveling")


    @leveling.command(name="channel", description="Setups a channel for leveling message")
    @commands.has_permissions(administrator = True)
    async def channel(self, ctx, *, channel: discord.TextChannel):
     # if not int(ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
      #  return await ctx.send("<a:cross:1088298797467193344> | Your top role should be above my top role.")
        with open("data.json", "r") as f:
            data = json.load(f)

        if str(ctx.author.id) not in data[str(ctx.guild.id)]:
            data[str(ctx.guild.id)][str(ctx.author.id)] = {}
            data[str(ctx.guild.id)][str(ctx.author.id)]["xp"] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]["level"] = 1

            with open("data.json", "w") as f:
                json.dump(data, f, indent = 4)

        else:
            pass

        with open("leveling.json", "r") as f:
            leveling = json.load(f)

        if str(ctx.guild.id) not in leveling:
            leveling[str(ctx.guild.id)] = {}
            leveling[str(ctx.guild.id)]["channel"] = int(channel.id)

            with open("leveling.json", "w") as f:
                json.dump(leveling, f, indent = 4)

            await ctx.send(f"<a:tick_vaibhavs_lithium:1166037808868237364> | Leveling channel has been set to {channel.mention}.")

        else:
            leveling[str(ctx.guild.id)]["channel"] = int(channel.id)

            with open("leveling.json", "w") as f:
                json.dump(leveling, f, indent = 4)

            await ctx.send(f"<a:tick_vaibhavs_lithium:1166037808868237364> | Leveling channel has been set to {channel.mention}.")


    @commands.hybrid_command(name="rank", aliases = ["level", "xp"])
    async def rank(self, ctx, member: discord.Member = None):
        with open("data.json", "r") as f:
            data = json.load(f)

        if str(ctx.author.id) not in data[str(ctx.guild.id)]:
            data[str(ctx.guild.id)][str(ctx.author.id)] = {}
            data[str(ctx.guild.id)][str(ctx.author.id)]["xp"] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]["level"] = 1

            with open("data.json", "w") as f:
                json.dump(data, f, indent = 4)


        with open("leveling.json", "r") as f:
            leveling = json.load(f)

        if str(ctx.guild.id) not in leveling:
            leveling[str(ctx.guild.id)] = {}
            leveling[str(ctx.guild.id)]["enabled"] = False

            with open("leveling.json", "w") as f:
                json.dump(leveling, f, indent = 4)

        if leveling[str(ctx.guild.id)]["enabled"] == True:
            if member == None:
                member = ctx.author


            with open("data.json", "r") as f:
                data = json.load(f)

            if str(member.id) not in data[str(ctx.guild.id)]:
                data[str(ctx.guild.id)][str(member.id)]["xp"] = 0
                data[str(ctx.guild.id)][str(member.id)]["level"] = 1

                with open("data.json", "w") as f:
                    json.dump(data, f, indent = 4)

                await ctx.send(f"{member.mention} is level 1 with 0 XP.")
        
            else:
                await ctx.send(f"{member.mention} is level {data[str(ctx.guild.id)][str(member.id)]['level']} with {data[str(ctx.guild.id)][str(member.id)]['xp']} XP.")
        else:
            await ctx.send("Leveling is not enabled, please enable the leveling first")


    @commands.command(name="leaderboard", aliases = ["lb"])
    async def leaderboard(self, ctx):
        with open("data.json", "r") as f:
            data = json.load(f)

        if str(ctx.author.id) not in data[str(ctx.guild.id)]:
            data[str(ctx.guild.id)][str(ctx.author.id)] = {}
            data[str(ctx.guild.id)][str(ctx.author.id)]["xp"] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]["level"] = 1

            with open("data.json", "w") as f:
                json.dump(data, f, indent = 4)

        else:
            pass

        with open("leveling.json", "r") as f:
            leveling = json.load(f)

        if str(ctx.guild.id) not in leveling:
            leveling[str(ctx.guild.id)] = {}
            leveling[str(ctx.guild.id)]["enabled"] = False

            with open("leveling.json", "w") as f:
                json.dump(leveling, f, indent = 4)

        if leveling[str(ctx.guild.id)]["enabled"] == True:
            with open("data.json", "r") as f:
                data = json.load(f)

            if str(ctx.guild.id) not in data:
                await ctx.send("There is no data for this server.")

            else:
                leaderboard = {}
                for user in data[str(ctx.guild.id)]:
                    leaderboard[user] = data[str(ctx.guild.id)][user]["level"]

                leaderboard = dict(sorted(leaderboard.items(), key = lambda item: item[1], reverse = True))

                embed = discord.Embed(title = "Leaderboard",color = discord.Color.green())
                embed.set_thumbnail(url = ctx.guild.icon)

                for user in leaderboard:
                    embed.add_field(name = f"{ctx.guild.get_member(int(user)).name}", value = f"Level: {data[str(ctx.guild.id)][user]['level']} | XP: {data[str(ctx.guild.id)][user]['xp']}\n", inline = False)

                await ctx.send(embed = embed)
        else:
            await ctx.send("Leveling is not enabled, please enable the leveling first")


    @commands.command(name="reset")
    @commands.has_permissions(administrator = True)
    async def reset(self, ctx, member: discord.Member = None):
     # if not int(ctx.author.top_role.position) > int(ctx.guild.me.top_role.position):
       # return await ctx.send("<a:cross:1088298797467193344> | Your top role should be above my top role.")
        with open("data.json", "r") as f:
            data = json.load(f)

        if str(ctx.author.id) not in data[str(ctx.guild.id)]:
            data[str(ctx.guild.id)][str(ctx.author.id)] = {}
            data[str(ctx.guild.id)][str(ctx.author.id)]["xp"] = 0
            data[str(ctx.guild.id)][str(ctx.author.id)]["level"] = 1

            with open("data.json", "w") as f:
                json.dump(data, f, indent = 4)

        else:
            pass

        with open("leveling.json", "r") as f:
            leveling = json.load(f)

        if str(ctx.guild.id) not in leveling:
            leveling[str(ctx.guild.id)] = {}
            leveling[str(ctx.guild.id)]["enabled"] = False

            with open("leveling.json", "w") as f:
                json.dump(leveling, f, indent = 4)

        if leveling[str(ctx.guild.id)]["enabled"] == True:
            if member == None:
                member = ctx.author

            with open("data.json", "r") as f:
                data = json.load(f)

            if str(ctx.guild.id) not in data:
                await ctx.send("There is no data for this server.")

            else:
                if str(member.id) not in data[str(ctx.guild.id)]:
                    await ctx.send("There is no data for this member.")

                else:
                    data[str(ctx.guild.id)][str(member.id)]["xp"] = 0
                    data[str(ctx.guild.id)][str(member.id)]["level"] = 1

                    with open("data.json", "w") as f:
                        json.dump(data, f, indent = 4)

                    await ctx.send(f"{member.mention} has been reset.")
        else:
            await ctx.send(f"{ctx.author.mention} chutiye, leveling is not enabled, first enable it.")
          