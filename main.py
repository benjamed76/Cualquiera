import os

import discord
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener el token
TOKEN = os.getenv("DISCORD_TOKEN")

# Configurar permisos
intents = discord.Intents.default()
intents.message_content = True

# Crear el cliente
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"✅ Conectado como {client.user}")


@client.event
async def on_message(message):

    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return

    # Comando !hola
    if message.content.lower() == "!hola":
        await message.channel.send(
            f"¡Hola {message.author.name}! 👋 Soy BotAtencion."
        )


client.run(TOKEN)