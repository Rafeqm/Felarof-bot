import discord
from discord.ext import commands

#---KAMUS CABANG---#


class Welcome(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.client.get_channel(799309066202775624) #ID channel yg dikirimin welcome message
        if not channel:
            return
        else:
            await channel.send(f"Welcome, {member.mention}!")


def setup(client):
    client.add_cog(Welcome(client))