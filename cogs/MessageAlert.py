import discord
from discord.ext import commands

#---KAMUS CABANG---#


class MessageAlert(commands.Cog):
    def __init__(self, client):
        self.client = client

    # [1] LINK ALERT!!
    @commands.Cog.listener()
    async def on_message(self, message):
        if "https://" in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Don't send links!")
            return
    # gak taulah knp kalo kirim link malah gak respon samsek
  
    # [2] KATA2 TAK SOPAN ALERT!!
    # bilang ke yg ngomong:
    @commands.Cog.listener()
    async def on_message(self, message):
        kataharam = ['anjing', 'babi', 'asu', 'kontol', 'pepek']
        for kata in kataharam:
            if kata in message.content.casefold(): # Go through the list of bad words
                await message.delete()
                await message.channel.send(f"{message.author.mention} Hati-hati kalo bicara!")
                self.client.dispatch('katataksopan', message, kata)
                return # So that it doesn't try to delete the message again.
    
    # bilang ke semua:
    @commands.Cog.listener()
    async def on_katataksopan(self, message, kata):
        #channel = client.get_channel(861297277150298153) #(channel id-nya) --> pake kalo mau send ke channel tertentu
        embed = discord.Embed(
            title="*ALERT*: Kata tak sopan",
            description=f"{message.author.name} just said ||{kata}||",
            color=discord.Color.red()
        )
        await message.channel.send(embed=embed)
        return

def setup(client):
    client.add_cog(MessageAlert(client))