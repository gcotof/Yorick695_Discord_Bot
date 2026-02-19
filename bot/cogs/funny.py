import discord
from discord.ext import commands
from pathlib import Path

class Funny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pat")
    async def pat(self, ctx):
        gif_path = Path(__file__).parent.parent / "gifs" / "yorickpat.gif"
        # __file__ = .../bot/cogs/funny.py
        # parent.parent = .../bot
        # luego /gifs/yorickpat.gif

        if not gif_path.exists():
            return await ctx.send(f"❌ No encontré el gif en: `{gif_path}`")

        file = discord.File(str(gif_path), filename="yorickpat.gif")
        await ctx.send(file=file)

async def setup(bot):
    await bot.add_cog(Funny(bot))
