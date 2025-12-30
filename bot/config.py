import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    token: str
    prefix: str

def get_settings() -> Settings:
    token = os.getenv("DISCORD_TOKEN", "").strip()
    prefix = os.getenv("COMMAND_PREFIX", "y!").strip()

    if not token:
        raise RuntimeError(
            "Falta DISCORD_TOKEN en el entorno. Crea un .env con DISCORD_TOKEN=..."
        )

    return Settings(token=token, prefix=prefix)
