import discord
from discord.ext import commands

from bot.dice.generic import parse_generic, roll_generic

class Dice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="roll")
    async def roll(self, ctx: commands.Context, expr: str = None):
        """
        Dados genéricos
        Uso:
          y!roll d20
          y!roll 2d8
          y!roll 3d6+2
          y!roll 4d10-1
        """
        if not expr:
            await ctx.reply("Uso: `y!roll d20`, `y!roll 2d8`, `y!roll 3d6+2`.", mention_author=False)
            return

        parsed = parse_generic(expr)
        if not parsed:
            await ctx.reply("Formato inválido. Ej: `d20`, `2d8`, `3d6+2`.", mention_author=False)
            return

        n, sides, modifier = parsed

        if n < 1 or n > 200:
            await ctx.reply("Cantidad de dados fuera de rango (1–200).", mention_author=False)
            return

        if sides < 2 or sides > 1000:
            await ctx.reply("Caras fuera de rango (2–1000).", mention_author=False)
            return

        result = roll_generic(n, sides, modifier)

        mod_txt = ""
        if result.modifier > 0:
            mod_txt = f" + {result.modifier}"
        elif result.modifier < 0:
            mod_txt = f" - {abs(result.modifier)}"

        rolls_txt = ", ".join(str(r) for r in result.rolls)

        embed = discord.Embed(
            title=f"{ctx.author.display_name} rolled {n}d{sides}{mod_txt}",
            description=f"Rolls: [{rolls_txt}]",
            color=0x2B2D31
        )
        embed.add_field(name="Total", value=f"**{result.total}**", inline=False)

        await ctx.send(content=f"{ctx.author.mention} rolled:", embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Dice(bot))
