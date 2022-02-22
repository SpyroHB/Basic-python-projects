import discord
from discord.ext import commands
from discord.ext.commands import bot
from config import BOT_TOKEN , prefix , owner_id
import asyncio
import time
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

intents = discord.Intents(messages=True, guilds=True, members=True)
# Imports the needed libs.

client = commands.Bot(command_prefix=prefix, intents=intents)
# Sets prefix and intents

client.remove_command("help")

@client.event
async def on_ready():
    print ("Ah shit, here we go again")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

####HELP COMMAND####
@client.command(pass_context=True)
async def secret(ctx):
    await ctx.message.delete()
    member = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Secret')
    embed.add_field(name='Ping', value='Gives ping to client (expressed in MS)', inline=False)
    embed.add_field(name='Info', value='Gives information of a user', inline=False)
    await member.send(embed=embed)
#############################


####PING COMMAND####
@client.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await member.send(embed=embed)
    print("Action completed: Server ping")
#############################

####INFO COMMAND####
@client.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print("Action completed: User Info")
#############################
client = MyClient()
client.run(BOT_TOKEN)