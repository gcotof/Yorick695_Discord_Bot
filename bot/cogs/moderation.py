from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="clean")
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx: commands.Context, amount: int = 20):
        if amount < 1 or amount > 100:
            await ctx.reply(
                "El número debe estar entre 1 y 100.",
                mention_author=False
            )
            return

        deleted = await ctx.channel.purge(limit=amount + 1)
        confirm = await ctx.send(f"🧹 {len(deleted) - 1} mensajes eliminados.")
        await confirm.delete(delay=3)

    @clean.error
    async def clean_error(self, ctx: commands.Context, error: Exception):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply(
                "Este comando solo puede ser usado por administradores.",
                mention_author=False
            )

async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot))
