import discord
import DiscordUtils  # from https://github.com/toxicrecker/DiscordUtils
from discord.ext import commands
from DiscordUtils.Music import Song

# ---KAMUS CABANG---#
music = DiscordUtils.Music()


class AudioPlayer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if not ctx.author.voice:  # Little from YT_Glowstik
            return await ctx.send("You're not currently in the voice channel")
        await ctx.author.voice.channel.connect()  # Joins author's voice channel
        await ctx.send("Joined your voice channel")

    @commands.command()
    async def leave(self, ctx):
        if not ctx.author.voice:
            return await ctx.send("You're not currently in the voice channel")
        mevoicetrue = ctx.guild.me.voice
        if not mevoicetrue:  # Little from YT_Glowstik
            return await ctx.send("I'm not currently in the voice channel")
        await ctx.voice_client.disconnect()
        await ctx.send("Left your voice channel")

    @commands.command()
    async def play(self, ctx, *, url):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = music.create_player(ctx, ffmpeg_error_fix=True, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True, bettersearch=True)
            song = await player.play()
            await ctx.send(f"Memutar: *`{song.name}`*.")
        else:
            song = await player.queue(url, search=True)
            await ctx.send(f"*`{song.name}`* ditambah ke daftar putar.")

    @commands.command()
    async def pause(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send(f"Paused *`{song.name}`*.")

    @commands.command()
    async def resume(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        await ctx.send(f"Resumed *`{song.name}`*.")

    @commands.command()
    async def stop(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        await player.stop()
        await ctx.send("Stopped")

    @commands.command()
    async def loop(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.toggle_song_loop()
        if song.is_looping:
            await ctx.send(f"*`{song.name}`* is looping!")
        else:
            await ctx.send(f"*`{song.name}`* is not looping!")

    @commands.command()
    async def playlist(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        daftar = player.current_queue()
        for index, song in enumerate(daftar):
            if daftar is not None:
                await ctx.send("Daftar putar:```" + "\n".join(str(index), ' ', song.name) + '```')
            else:
                await ctx.send("Playlist lagi kosong")

    @commands.command()
    async def nowplaying(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = player.now_playing()
        await ctx.send(f"Sedang memutar *`{song.name}`*.")

    @commands.command()
    async def skip(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        data = await player.skip(force=True)
        if len(data) == 2:
            await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
        else:
            await ctx.send(f"Skipped {data[0].name}")

    @commands.command()
    async def volume(self, ctx, vol):
        player = music.get_player(guild_id=ctx.guild.id)
        song, volume = await player.change_volume(float(vol) / 100)  # volume should be a float between 0 to 1
        await ctx.send(f"Changed volume for {song.name} to {volume*100}%")

    @commands.command()
    async def remove(self, ctx, index):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.remove_from_queue(int(index))
        await self.message.channel.send(f"*`{song.name}`* dihapus dari daftar putar.")


def setup(client):
    client.add_cog(AudioPlayer(client))
