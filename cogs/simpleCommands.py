import time

import discord
from discord.ext import commands

#---KAMUS CABANG---#


class SimpleCommands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, client):
        self.client = client

    @commands.command(name='hello', brief="Sapa member!")
    async def hello(self, ctx):
        await ctx.send(f"Hi **{ctx.author.name}**!")
        return
    
    @commands.command(name='ping', brief="Get the bot's current websocket latency and API latency.")
    async def ping(self, ctx):
        
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"Pong! {round(self.client.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")

    @commands.command()
    @commands.is_owner()
    async def act(self, ctx, *args):
        game = discord.Game(args)
        await self.client.change_presence(activity=game)

#    @commands.command(name='users', description='jumlah anggota server')
#    async def users(self, ctx):
#            guild = self.client.get_guild(860877935706505216)
#            await ctx.send(f'# of {id.member_count}')

def setup(client):
    client.add_cog(SimpleCommands(client))
