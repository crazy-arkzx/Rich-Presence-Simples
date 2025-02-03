# SISTEMA DE RICH PRESENCE SIMPLES PARA SEU BOT
# FEITO POR: Crazy_ArKzX
# GitHub: https://github.com/crazy-arkzx

import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="Titulo" # Titulo da sua Rich Presence
        )
    )
    print("Rich Presence Carregada com Sucesso!")

bot.run("SEU_TOKEN")