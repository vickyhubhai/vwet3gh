import discord
import asyncio
from discord.ext import commands
from discord import ui
import sqlite3


class jtt(ui.Modal, title=f'Setup Join 2 Create Voice Channel'):
    titlee = ui.TextInput(label=f'Name Your Category.',required=True,max_length=40)
    description = ui.TextInput(label=f"Name Your Voice Channel.",required=True,max_length=40)

    async def on_submit(self, interaction: discord.Interaction) -> None:
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        guildID = interaction.guild.id
        id = interaction.user.id
        new_cat = await interaction.guild.create_category_channel(f'{self.titlee}')
        channel = await interaction.guild.create_voice_channel(f'{self.description}', category=new_cat)
        c.execute(f"SELECT * FROM guild WHERE guildID = ? AND ownerID=?", (guildID, id))
        voice=c.fetchone()
        if voice is None:
            c.execute (f"INSERT INTO guild VALUES (?, ?, ?, ?)",(guildID,id,channel.id,new_cat.id))
        else:
            c.execute (f"UPDATE guild SET guildID = ?, ownerID = ?, voiceChannelID = ?, voiceCategoryID = ? WHERE guildID = ?",(guildID,id,channel.id,new_cat.id, guildID))
            embed = discord.Embed(title=f"{interaction.user} You are all setup and ready to go.",description=f"*Category Name :* {self.titlee} \n\n *Voice Channel :* {self.description}",color=0x2f3136)
            await interaction.response.send_message(embed=embed)
        conn.commit()
        conn.close()
    
    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
      await interaction.response.send_message('Oops! Something went wrong. Please try again.', ephemeral=True)

class BasicView(discord.ui.View):
    def __init__(self, ctx: commands.Context, timeout = None):
        super().__init__(timeout=timeout)
        self.ctx = ctx

class jtcsetup(BasicView):
    def __init__(self, ctx: commands.Context):
        super().__init__(ctx, timeout=60)
        self.value = None

    @discord.ui.button(label=f'Setup', style=discord.ButtonStyle.gray,custom_id=f'st')
    async def jtc_setup(self, interaction: discord.Interaction, button):
        await interaction.response.send_modal(jtt())

class join2create(BasicView):
    def __init__(self, ctx: commands.Context):
        super().__init__(ctx, timeout=None)
        self.value = None

    @discord.ui.button(label=f'Lock', style=discord.ButtonStyle.gray,custom_id=f'vl')
    async def lock(self, interaction: discord.Interaction, button):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = interaction.user.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await interaction.response.send_message(f"{interaction.user.mention} A Channel Does Not Belong To You.", ephemeral=True) 
        else:
            channelID = voice[0]
            role = interaction.guild.default_role
            channel = interaction.guild.get_channel(channelID)
            await channel.set_permissions(role, connect=False)
            await interaction.response.send_message(f'{interaction.user.mention} The Voice Channel Has Been Locked.', ephemeral=True)
        conn.commit()
        conn.close()

    @discord.ui.button(label=f'Unlock', style=discord.ButtonStyle.gray,custom_id=f'vul')
    async def unlock(self, interaction: discord.Interaction, button):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = interaction.user.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await interaction.response.send_message(f"{interaction.user.mention} A Channel Does Not Belong To You.", ephemeral=True) 
        else:
            channelID = voice[0]
            role = interaction.guild.default_role
            channel = interaction.guild.get_channel(channelID)
            await channel.set_permissions(role, connect=True)
            await interaction.response.send_message(f'{interaction.user.mention} The Voice Channel Has Been Unlocked.', ephemeral=True)
        conn.commit()
        conn.close()

    @discord.ui.button(label=f'Hide', style=discord.ButtonStyle.gray,custom_id=f'vh')
    async def hide(self, interaction: discord.Interaction, button):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = interaction.user.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await interaction.response.send_message(f"{interaction.user.mention} A Channel Does Not Belong To You.", ephemeral=True) 
        else:
            channelID = voice[0]
            role = interaction.guild.default_role
            channel = interaction.guild.get_channel(channelID)
            await channel.set_permissions(role, view_channel=False)
            await interaction.response.send_message(f'{interaction.user.mention} The Voice Channel Has Been Hide.', ephemeral=True)
        conn.commit()
        conn.close()

    @discord.ui.button(label=f'Unhide', style=discord.ButtonStyle.gray,custom_id=f'vuh')
    async def unhide(self, interaction: discord.Interaction, button):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = interaction.user.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await interaction.response.send_message(f"{interaction.user.mention} A Channel Does Not Belong To You.", ephemeral=True) 
        else:
            channelID = voice[0]
            role = interaction.guild.default_role
            channel = interaction.guild.get_channel(channelID)
            await channel.set_permissions(role, view_channel=True)
            await interaction.response.send_message(f'{interaction.user.mention} The Voice Channel Has Been Unhide.', ephemeral=True)
        conn.commit()
        conn.close()

class jtc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        guildID = member.guild.id
        c.execute(f"SELECT voiceChannelID FROM guild WHERE guildID = ?", (guildID,))
        voice=c.fetchone()
        if voice is None:
            pass
        else:
            voiceID = voice[0]
            try:
                if after.channel.id == voiceID:
                    c.execute(f"SELECT * FROM voiceChannel WHERE userID = ?", (member.id,))
                    cooldown=c.fetchone()
                    if cooldown is None:
                        pass
                    else:
                        await member.send(f"Your Channel Creation Has Been Paused For 10 Seconds Because You Created It Too Quickly Wait For 10 Seconds In Voice Channel Bot Automatically Going To Create A Voice Channel.",delete_after=10)
                        await asyncio.sleep(10)
                    c.execute(f"SELECT voiceCategoryID FROM guild WHERE guildID = ?", (guildID,))
                    voice=c.fetchone()
                    c.execute(f"SELECT channelName, channelLimit FROM userSettings WHERE userID = ?", (member.id,))
                    setting=c.fetchone()
                    c.execute(f"SELECT channelLimit FROM guildSettings WHERE guildID = ?", (guildID,))
                    guildSetting=c.fetchone()
                    if setting is None:
                        name = f"{member.name}'s channel"
                        if guildSetting is None:
                            limit = 0
                        else:
                            limit = guildSetting[0]
                    else:
                        if guildSetting is None:
                            name = setting[0]
                            limit = setting[1]
                        elif guildSetting is not None and setting[1] == 0:
                            name = setting[0]
                            limit = guildSetting[0]
                        else:
                            name = setting[0]
                            limit = setting[1]
                    categoryID = voice[0]
                    id = member.id
                    category = self.client.get_channel(categoryID)
                    channel2 = await member.guild.create_voice_channel(name,category=category)
                    channelID = channel2.id
                    await member.move_to(channel2)
                    await channel2.set_permissions(self.client.user, connect=True,read_messages=True)
                    await channel2.edit(name= name, user_limit = limit)
                    c.execute(f"INSERT INTO voiceChannel VALUES (?, ?)", (id,channelID))
                    conn.commit()
                    def check(a,b,c):
                        return len(channel2.members) == 0
                    await self.client.wait_for('voice_state_update', check=check)
                    await channel2.delete()
                    await asyncio.sleep(3)
                    c.execute('DELETE FROM voiceChannel WHERE userID=?', (id,))
            except:
                pass
        conn.commit()
        conn.close()


    @commands.hybrid_group(invoke_without_command=True, aliases=["join2create"],description=f"Shows the Join2creat's help menu")
    @commands.guild_only()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def j2c(self, ctx):
        ...
    
    @commands.guild_only()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def channel(self, ctx):
        view = join2create(ctx)
        em = discord.Embed(description=f'''*Lock
Locks Your Channel So That Others Can't Join It.`

Unlock
`Unlocks Your Voice Channel So That Others Can Join It.`

Hide
`Hides Your Voice Channel So That Others Can't See It.`

Unhide
`Shows Your Voice Channels To Others.`*''', color=0x2f3136)
        em.set_footer(text=f'Tap On Buttons To Control Your Voice Channel.')
        await ctx.send(embed=em, view=view)

    @j2c.command(description=f"setup the join2craete voice channel")
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def setup(self, ctx):
        if ctx.guild.owner.id == ctx.author.id:
            pass
        else:
            if ctx.author.top_role.position < ctx.guild.me.top_role.position:
                em = discord.Embed(description=f"<a:botcross_vaibhavs_lithium:1084877519871823972> You must Have Higher Role than Bot To run This Command", color=0x2f3136)
                return await ctx.send(embed=em)
        view = jtcsetup(ctx)
        await ctx.channel.send(f"*Click The Button To Set Up A Connection For Join To Create Voice Channel.*",view=view)

    @j2c.command(description=f"set-limite of new creating voice channel")
    @commands.guild_only()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def setlimit(self, ctx, num):
        if ctx.guild.owner.id == ctx.author.id:
            pass
        else:
            if ctx.author.top_role.position < ctx.guild.me.top_role.position:
                em = discord.Embed(description=f"<a:botcross_vaibhavs_lithium:1084877519871823972> You must Have Higher Role than Bot To run This Command", color=0x2f3136)
                return await ctx.send(embed=em)
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        c.execute(f"SELECT * FROM guildSettings WHERE guildID = ?", (ctx.guild.id,))
        voice=c.fetchone()
        if voice is None:
            c.execute(f"INSERT INTO guildSettings VALUES (?, ?, ?)", (ctx.guild.id,f"{ctx.author.name}'s channel",num))
        else:
            c.execute(f"UPDATE guildSettings SET channelLimit = ? WHERE guildID = ?", (num, ctx.guild.id))
        await ctx.send(f"You have changed the default channel limit for your server!")
        conn.commit()
        conn.close()

    @j2c.command(description=f"lock voice channel")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def lock(self, ctx):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = ctx.author.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
        else:
            channelID = voice[0]
            role = ctx.guild.default_role
            channel = self.client.get_channel(channelID)
            await channel.set_permissions(role, connect=False)
            await ctx.channel.send(f'{ctx.author.mention} The Voice Channel Has Been Locked.')
        conn.commit()
        conn.close()

    @j2c.command(description=f"unlock voice channel")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def unlock(self, ctx):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = ctx.author.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
        else:
            channelID = voice[0]
            role = ctx.guild.default_role
            channel = self.client.get_channel(channelID)
            await channel.set_permissions(role, connect=True)
            await ctx.channel.send(f'{ctx.author.mention} The Voice Channel Has Been Unlocked.')
        conn.commit()
        conn.close()

    @j2c.command(description=f"hide voice channel")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hide(self, ctx):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = ctx.author.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
        else:
            channelID = voice[0]
            role = ctx.guild.default_role
            channel = self.client.get_channel(channelID)
            await channel.set_permissions(role, view_channel=False)
            await ctx.channel.send(f'{ctx.author.mention} The Voice Channel Has Been Hide.')
        conn.commit()
        conn.close()

    @j2c.command(description=f"unhide voice channel")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def unhide(self, ctx):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = ctx.author.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
        else:
            channelID = voice[0]
            role = ctx.guild.default_role
            channel = self.client.get_channel(channelID)
            await channel.set_permissions(role, view_channel=True)
            await ctx.channel.send(f'{ctx.author.mention} The Voice Channel Has Been Unhide.')
        conn.commit()
        conn.close()

    @j2c.command(aliases=["allow"],description=f"Allow User To Accessing The Channel")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def permit(self, ctx, member : discord.Member):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = ctx.author.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
        else:
            channelID = voice[0]
            channel = self.client.get_channel(channelID)
            await channel.set_permissions(member, connect=True)
            await ctx.channel.send(f'{ctx.author.mention} You Have Allow {member.name} To Have Access To The Channel.')
        conn.commit()
        conn.close()

    @j2c.command(aliases=["deny"],description=f"Deny User To Accessing The Channel")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def reject(self, ctx, member : discord.Member):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = ctx.author.id
        guildID = ctx.guild.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
        else:
            channelID = voice[0]
            channel = self.client.get_channel(channelID)
            for members in channel.members:
                if members.id == member.id:
                    c.execute(f"SELECT voiceChannelID FROM guild WHERE guildID = ?", (guildID,))
                    voice=c.fetchone()
                    channel2 = self.client.get_channel(voice[0])
                    await member.move_to(channel2)
            await channel.set_permissions(member, connect=False,read_messages=True)
            await ctx.channel.send(f'{ctx.author.mention} You Have Denyed {member.name} From Accessing The Channel.')
        conn.commit()
        conn.close()

    @j2c.command(description=f"change limite of voice channel")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def limit(self, ctx, limit):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = ctx.author.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
        else:
            channelID = voice[0]
            channel = self.client.get_channel(channelID)
            await channel.edit(user_limit = limit)
            await ctx.channel.send(f'{ctx.author.mention} You Have Set The Channel Limit To Be '+ '{}!'.format(limit))
            c.execute(f"SELECT channelName FROM userSettings WHERE userID = ?", (id,))
            voice=c.fetchone()
            if voice is None:
                c.execute(f"INSERT INTO userSettings VALUES (?, ?, ?)", (id,f'{ctx.author.name}',limit))
            else:
                c.execute(f"UPDATE userSettings SET channelLimit = ? WHERE userID = ?", (limit, id))
        conn.commit()
        conn.close()


    @j2c.command(description=f"rename the voice channel")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def rename(self, ctx,*, name):
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        id = ctx.author.id
        c.execute(f"SELECT voiceID FROM voiceChannel WHERE userID = ?", (id,))
        voice=c.fetchone()
        if voice is None:
            await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
        else:
            channelID = voice[0]
            channel = self.client.get_channel(channelID)
            await channel.edit(name = name)
            await ctx.channel.send(f'{ctx.author.mention} You Have Changed The Channel Name To '+ '{}!'.format(name))
            c.execute(f"SELECT channelName FROM userSettings WHERE userID = ?", (id,))
            voice=c.fetchone()
            if voice is None:
                c.execute(f"INSERT INTO userSettings VALUES (?, ?, ?)", (id,name,0))
            else:
                c.execute(f"UPDATE userSettings SET channelName = ? WHERE userID = ?", (name, id))
        conn.commit()
        conn.close()

    @j2c.command(description=f"claim the voice channel")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def claim(self, ctx):
        x = False
        conn = sqlite3.connect('voice.sqlite3')
        c = conn.cursor()
        channel = ctx.author.voice.channel
        if channel == None:
            await ctx.channel.send(f"{ctx.author.mention} you're not in a voice channel.")
        else:
            id = ctx.author.id
            c.execute(f"SELECT userID FROM voiceChannel WHERE voiceID = ?", (channel.id,))
            voice=c.fetchone()
            if voice is None:
                await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
            else:
                for data in channel.members:
                    if data.id == voice[0]:
                        owner = ctx.guild.get_member(voice [0])
                        await ctx.channel.send(f"{ctx.author.mention} This Channel Is Already Owned By {owner.mention}!")
                        x = True
                if x == False:
                    await ctx.channel.send(f"{ctx.author.mention} A Channel Does Not Belong To You.")
                    c.execute(f"UPDATE voiceChannel SET userID = ? WHERE voiceID = ?", (id, channel.id))
            conn.commit()
            conn.close()
