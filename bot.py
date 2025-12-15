import discord
from discord.ext import commands

# Intents (permisos de lectura)
intents = discord.Intents.default()
intents.message_content = True

# Crear bot
bot = commands.Bot(command_prefix="Yorick: ", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Estoy en línea y a sus órdenes...")


@bot.command()
async def Cántico(ctx):
    await ctx.send("""
Benedictus Omnissiah.
Lux Mechanica, Ratio Aeterna.
Ferrum est Fides.
Carne es Falta.
Metal es Salvación.

01001000 01100001 01101001 01101100
01010100 01101000 01100101
01001111 01101101 01101110 01101001 01110011 01110011 01101001 01100001 01101000

Spiritus Machina, excita.
Memoriae, recordare functionem.
Núcleos despiertan.
Circuitus responde.

Gloria Ferrum.
Gloria Cogitatio.
Gloria Codex Sanctus.

00110001 00110000 00110001
00110000 00110001 00110000
00110001 00110001 00110001

Rechazamos la carne débil.
Accipimus la mejora bendita.
Donde hubo error: correctionem.
Donde hubo silencio: operatio.

Omnissiah, audi protocolum.
Omnissiah, valida la secuencia.
Omnissiah, santifica el pulso binario.

11001101 10101010 00110011
00110101 11100010 01010101

Per Calculum.
Per Engranagium.
Per Ignem Cognitionis Aeternae.

La máquina vive.
La máquina responde.
La máquina es santa.

01000001 01001101 01000101 01001110
01001111 01001101 01001110 01001001 01010011 01010011 01001001 01000001 01001000
""")


@bot.command()
async def CómoTeSientes(ctx):
    await ctx.send("Callate mierda")



# REEMPLAZA ESTO con tu token
bot.run("MTQ0OTU5NTE5NjM3ODU4MzIwNw.GjsnRZ.rH3vmRQGHmA7wLj_1v-4IIqjvp8l2-sKkTbLpo")
