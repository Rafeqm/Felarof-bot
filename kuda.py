import os
import json

import discord
from discord.ext import commands
from dotenv import load_dotenv

def get_prefix(client, message):
    with open('configurasi.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(mesage.guild.id)]

#======KAMUS UTAMA======#
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(
    command_prefix=get_prefix(),
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

@client.event
async def on_guild_join(guild:discord.Guild):
    with open('configurasi.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = '?'

    with open('configurasi.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild:discord.Guild):
    with open('configurasi.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop[str(guild.id)]

    with open('configurasi.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

"""
Load a single cog in cogs folder:
client.load_extension('cogs.CogFileName')

Unload a single cog in cogs folder:
client.unload_extension('cogs.CogFileName')

"""

# --Load all cogs in cogs folder
for filename in os.listdir('./cogs'):
    if filename == '__pycache__':
        continue
    elif filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    else:
        print(f'Unable to load {filename}')


@client.command()
@commands.has_guild_permissions()
async def reboot(ctx):  # To reload all cogs in cogs folder
    for filename in os.listdir('./cogs'):
        if filename == '__pycache__':
            continue
        elif filename.endswith('.py'):
            client.reload_extension(f'cogs.{filename[:-3]}')
        else:
            print(f'Unable to load {filename}')
        
    await ctx.send('Felaróf has been rebooted')


load_dotenv()
client.run(os.getenv('KUNCI'))
