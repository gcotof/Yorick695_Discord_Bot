import discord
from bot.config import get_settings
from bot.core.bot import YorickBot

def main() -> None:
    settings = get_settings()

    intents = discord.Intents.default()
    intents.message_content = True  # requerido para leer contenido de mensajes

    bot = YorickBot(command_prefix=settings.prefix, intents=intents)
    bot.run(settings.token)

if __name__ == "__main__":
    main()
