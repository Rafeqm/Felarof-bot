import discord
import DiscordUtils
from discord.ext import commands
from DiscordUtils.Music import Song

#---KAMUS CABANG---#
music = DiscordUtils.Music()


class BaseCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):  # from YT_Glowstik
        voicetrue = ctx.author.voice
        if voicetrue is None:
            return await ctx.send("You're not currently in the voice channel")
        await ctx.author.voice.channel.connect()
        await ctx.send("Joined your voice channel")
    
    @commands.command()
    async def leave(self, ctx):  # from YT_Glowstik
        voicetrue = ctx.author.voice
        mevoicetrue = ctx.guild.me.voice
        if voicetrue is None:
            return await ctx.send("You're not currently in the voice channel")
        if mevoicetrue is None:
            return await ctx.send("I'm not currently in the voice channel")
        await ctx.voice_client.disconnect()
        await ctx.send("Left your voice channel")
    
    @commands.command()
    async def play(self, ctx, *, url):  # from YT_Glowstik
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            await ctx.send(f'Memutar: `*{song.name}*`')
        else:
            song = await player.queue(url, search=True)
            await ctx.send(f'`*{song.name}*` ditambah ke daftar putar')
    
    @commands.command()
    async def playlist(self, ctx):  # improvised, from YT_Glowstik
        player = music.get_player(guild_id=ctx.guild.id)
        await ctx.send(f"Daftar putar:\n```{' |#| '.join([song.name for song in player.current_queue()])}```")
    
    @commands.command()
    async def pause(self, ctx):  # from YT_Glowstik
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send(f'Paused `*{song.name}*`')
    
    @commands.command()
    async def resume(self, ctx):  # from YT_Glowstik
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        await ctx.send(f'Resumed `*{song.name}*`')
    
    @commands.command()
    async def loop(self, ctx):  # from YT_Glowstik
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.toggle_song_loop()
        if song.is_looping:
            return await ctx.send(f'`*{song.name}*` is looping!')
        else:
            return await ctx.send(f'`*{song.name}*` is not looping!')
    
    @commands.command()
    async def nowplaying(self, ctx):  # from YT_Glowstik
        player = music.get_player(guild_id=ctx.guild.id)
        song = player.now_playing()
        await ctx.send(f'Sedang memutar `*{song.name}*`.')
    
    @commands.command()
    async def remove(self, ctx, index):  # from YT_Glowstik
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.remove_from_queue(int(index))
        await self.message.channel.send(f'`*{song.name}*` dihapus dari daftar putar.')


def setup(client):
    client.add_cog(BaseCog(client))
