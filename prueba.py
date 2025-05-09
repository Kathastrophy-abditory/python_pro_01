import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def en_lines():
    print(f'Tu bot {bot.user} esta en linea')

@bot.command()
async def saludar(ctx,*,mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        await ctx.send('Hola, ¿cómo estás?')
    elif mensaje == 'klk':
        await ctx.send('Klk, ¿todo bien?')
    elif mensaje == 'buenas':
        await ctx.send('Buenas, ¿qué tal?')
    else:
        await ctx.send('SALUDA BIEN!!!')

@bot.command()
async def suma(ctx, left: int, right: int):
    await ctx.send(f'Result: {left + right}')

token = ""

bot.run(token)