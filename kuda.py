import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


#======KAMUS UTAMA======#
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(
    command_prefix="?",
    case_insensitive=True,
    intents=intents,
    allowed_mentions=discord.AllowedMentions(
        users=True,         # Whether to ping individual user @mentions
        everyone=False,      # Whether to ping @everyone or @here mentions
        roles=False,         # Whether to ping role @mentions
        replied_user=True  # Whether to ping on replies to messages
    )
)

#======KODE======#
@client.event
async def on_ready():
    print(f'I now live as {client.user} to serve you, My Lord!')

"""
Load a single cog in cogs folder:
client.load_extension('cogs.CogFileName')

Unload a single cog in cogs folder:
client.unload_extension('cogs.CogFileName')
"""

# --Load all cogs in cogs folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    else:
        print(f'Unable to load {filename}')


@client.command()
@commands.has_guild_permissions()
async def reboot(ctx):  # To reload all cogs in cogs folder
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.reload_extension(f'cogs.{filename[:-3]}')
        else:
            print(f'Unable to load {filename}')
        
    await ctx.send('Felaróf has been rebooted')


load_dotenv()
client.run(os.getenv('KUNCI'))
