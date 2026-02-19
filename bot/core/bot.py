import discord
from discord.ext import commands

DEFAULT_EXTENSIONS = (
    "bot.cogs.ping",
    "bot.cogs.moderation",
    "bot.cogs.dice",
    "bot.cogs.wrath_and_glory",
    "bot.cogs.funny",
)

class YorickBot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def setup_hook(self) -> None:
        # Cargar Cogs al arrancar
        for ext in DEFAULT_EXTENSIONS:
            await self.load_extension(ext)

    async def on_ready(self) -> None:
        print(f"Bot conectado como {self.user} (ID: {self.user.id})")
