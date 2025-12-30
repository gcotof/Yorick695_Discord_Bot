import discord
from discord.ext import commands

from bot.dice.wrath_and_glory import parse_expr, roll_wg, render_wg

class WrathAndGlory(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="wroll")
    async def wroll(self, ctx: commands.Context, expr: str = None):
        """
        Wrath & Glory dice pool (d6 only)
        Uso: y!wroll 8d6  |  y!wroll d6
        """
        if not expr:
            await ctx.reply("Uso: `y!wroll 8d6` (ej: `y!wroll d6`).", mention_author=False)
            return

        parsed = parse_expr(expr)
        if not parsed:
            await ctx.reply("Formato inválido. Usa `NdM` como `8d6` o `d6`.", mention_author=False)
            return

        n, sides = parsed

        if sides != 6:
            await ctx.reply("Wrath & Glory usa solo d6. Ej: `y!wroll 8d6`.", mention_author=False)
            return

        if n < 1 or n > 100:
            await ctx.reply("Cantidad de dados fuera de rango (1–100).", mention_author=False)
            return

        result = roll_wg(n)
        rendered = render_wg(result)

        wrath_note = f"Wrath Die: **{result.wrath}**"
        if result.wrath == 6:
            wrath_note += " (Exalted)"
        elif result.wrath == 1:
            wrath_note += " (Complication)"

        summary = (
            f"Éxitos (4+): **{result.successes}** | 6s: **{result.sixes}** | 1s: **{result.ones}**\n"
            f"{wrath_note}"
        )

        embed = discord.Embed(
            title=f"{ctx.author.display_name} rolled {n}d6 (W&G)",
            description=rendered,
            color=0x2B2D31
        )
        embed.add_field(name="Resumen", value=summary, inline=False)

        await ctx.send(content=f"{ctx.author.mention} rolled:", embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(WrathAndGlory(bot))
