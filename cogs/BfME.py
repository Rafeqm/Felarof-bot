import discord
import DiscordUtils
from discord import embeds  # from https://github.com/toxicrecker/DiscordUtils
from discord.ext import commands

# ---KAMUS CABANG---#
rafeq = "https://instagram.com/rafeqm_"
rafeq_ava = "https://www.gamereplays.org/community/uploads/av-923619.jpg"

BfME_dict = {

}
gamereplays = f"[Gamereplays.org](https://www.gamereplays.org)"
gamereplays_ico = ""
BFME = "Battle for Middle-Earth"
BFME_old = "https://forums.revora.net/topic/105190-bfme1bfme2rotwk-games-download-installation-guide"
BFME_thumbnail = "https://cutt.ly/BQm9J8t"
BFME1_main = f"[{BFME}](https://www.gamereplays.org/community/index.php?showtopic=1054012)"
BFME1_103 = f"[Patch 1.03](https://www.gamereplays.org/battleformiddleearth/portals.php?show=page&name=patch-103-downloads)"
BFME1_106 = f"[Patch 1.06](https://www.gamereplays.org/community/index.php?showtopic=979783)"
BFME1_109 = f"[Patch 1.09](https://www.gamereplays.org/battleformiddleearth/portals.php?show=page&name=109%20Patch)"
BFME2 = f"{BFME} II"
BFME2_main = f"[{BFME2}](https://www.gamereplays.org/battleformiddleearth2/portals.php?show=page&name=bfme2-no-cd-guide-patch-1.09-crack)"
BFME2_106 = f"[Patch 1.06](https://www.gamefront.com/games/battle-for-middle-earth-2/file/bfme-2-1-06-patch-english)"
BFME2_109 = f"[Patch 1.09](https://www.gamereplays.org/battleformiddleearth2/portals.php?show=page&name=bfme2-patch-1.09-version-2.0-live)"
RotWK = f"{BFME2}: Rise of The Witch-King"
RotWK_main = f"[{RotWK}](https://www.gamereplays.org/community/index.php?showtopic=1006906)"
RotWK_201 = f"[Patch 2.01](https://www.gamereplays.org/riseofthewitchking/portals.php?show=page&name=rotwk-official-2.01-downloads)"
RotWK_202 = f"[Patch 2.02](https://www.gamereplays.org/riseofthewitchking/portals.php?show=page&name=unofficial-patch-202-download-page)"
BFMER = f"{BFME}: Reforged"
BFMER_main = f"[{BFME}: Reforged](https://bfmereforged.org)"
BFME_main = [BFME1_main, BFME2_main, RotWK_main]


class Game(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="bfme", brief=f"Download dan install {BFME}")
    async def bfme(self, ctx):
        embed1 = discord.Embed(
            title=f"**{BFME}**",
            description=f"Cara unduh dan pasang serial game {BFME}:\n" + "\n".join(f"**•\t{BFME_main[x]}**" for x in range(len(BFME_main))),
            color=discord.Color.gold(),
        )
        embed1.set_author(name="Éofèq", url=rafeq, icon_url=rafeq_ava)
        embed1.add_field(name="Catatan:", value=f"Silakan baca [artikel utama ini]({BFME_old}) jika Anda mendapat error.")
        embed1.set_thumbnail(url=BFME_thumbnail)
        embed1.set_footer(text=f"- didukung oleh Gamereplays.org", icon_url=gamereplays_ico)
        

        embed2 = discord.Embed(
            title=f"Patches for **{BFME}**",
            description=f"Unduh patch untuk serial game {BFME}:",
            color=discord.Color.orange(),
        )
        embed2.set_author(name="Éofèq", url=rafeq, icon_url=rafeq_ava)
        embed2.add_field(
            name=f"{BFME}:",
            value=f"•\t{BFME1_103} (wajib)\n•\t{BFME1_106}\n•\t{BFME1_109} (not recommended)",
            inline=False,
        )
        embed2.add_field(name=f"{BFME2}:", value=f"•\t{BFME2_109} (All-in-one)", inline=False)
        embed2.add_field(
            name=f"{RotWK}:",
            value=f"•\t{RotWK_201} (wajib)\n•\t{RotWK_202}",
            inline=False,
        )
        embed2.set_thumbnail(url=BFME_thumbnail)
        embed2.set_footer(text=f"- didukung oleh Gamereplays.org", icon_url=gamereplays_ico)


        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('🔐', "lock")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        embeds = [embed1, embed2]
        await paginator.run(embeds)


def setup(client):
    client.add_cog(Game(client))
