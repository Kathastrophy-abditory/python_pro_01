import discord
from discord.ext import commands
import random
import os
import requests 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

datos_random = [
    "La iluminación urbana excesiva impide ver el cielo nocturno y daña la salud de las personas y animales.",
    "Muchas personas aún usan focos incandescentes o fríos que gastan más electricidad y contaminan más.",
    "Si vives cerca de zonas rurales o áreas naturales, incluso una pequeña luz constante en el exterior puede afectar la visibilidad del cielo.",
    "Las luces artificiales desorientan a los animales que se guían por la luz natural. Esto también interfiere en los ecosistemas cercanos a zonas habitadas.",
    "Las luces innecesarias, incluso en casas o negocios pequeños, contribuyen al problema cuando están mal dirigidas o encendidas todo el tiempo.",
    "Muchas veces se dejan luces prendidas por costumbre, sin necesidad real.",
    "Aunque aún no hay normas federales claras, sí puedes tomar decisiones conscientes desde casa."
]

soluciones_random = [
    "Usa cortinas opacas o blackout en ventanas exteriores para que la luz de tu hogar no se disperse hacia la calle o cielo. Esto ayuda a reducir el “resplandor urbano” sin complicaciones.",
    "Cambia tus focos por LED cálidos (etiquetados como “luz cálida” o <3000K). Consumen menos energía, duran más y producen menos contaminación lumínica.",
    "Apaga las luces exteriores durante la noche si no son necesarias. Si usas luz para seguridad, opta por lámparas con sensores de movimiento que se enciendan solo cuando haya alguien cerca.",
    "Evita dejar luces encendidas toda la noche en jardines, patios o terrazas. Si necesitas iluminación nocturna, usa lámparas solares con luz cálida y temporizador.",
    "Revisa cuántas luces decorativas tienes encendidas cada noche. Apaga las que no sean esenciales y considera usar iluminación tenue en vez de brillante para ambientes acogedores sin derroche.",
    "Haz el hábito de revisar tu casa antes de dormir para apagar luces innecesarias. Puedes hacer una lista visual en tu refri o una alarma en tu celular como recordatorio.",
    "Comparte lo que aprendes sobre contaminación lumínica con tu familia y vecinos. Hablar del tema es el primer paso para generar un cambio colectivo."
]

luminosidad_estados = {
    "Aguascalientes": "7-8",
    "Baja California": "3-8",
    "Baja California Sur": "4-6",
    "Campeche": "3-5",
    "Chiapas": "2-6",
    "Chihuahua": "4-9",
    "Ciudad de México": "9",
    "Coahuila": "4-7",
    "Colima": "5-7",
    "Durango": "3-5",
    "Estado de México": "8-9",
    "Guanajuato": "6-8",
    "Guerrero": "4-6",
    "Hidalgo": "4-6",
    "Jalisco": "5-9",
    "Michoacán": "3-6",
    "Morelos": "6-8",
    "Nayarit": "4-6",
    "Nuevo León": "8-9",
    "Oaxaca": "2-5",
    "Puebla": "7-9",
    "Querétaro": "5-7",
    "Quintana Roo": "4-6",
    "San Luis Potosí": "5-7",
    "Sinaloa": "5-7",
    "Sonora": "3-6",
    "Tabasco": "5-7",
    "Tamaulipas": "5-7",
    "Tlaxcala": "6-7",
    "Veracruz": "5-7",
    "Yucatán": "4-6",
    "Zacatecas": "4-6"
}


@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea')

@bot.command("Datos")
async def datos(ctx):
    dato = random.choice(datos_random)
    await ctx.send(dato)

@bot.command("Soluciones")
async def soluciones(ctx):
    solucion = random.choice(soluciones_random)
    await ctx.send(solucion)

@bot.command("Definicion")
async def definicion(ctx):
    await ctx.send("La contaminación lumínica ocurre cuando usamos demasiada luz artificial o la usamos mal (por ejemplo, apuntando al cielo o dejándola encendida sin necesidad). Este tipo de contaminación ilumina de más nuestras ciudades, hogares y calles, impidiendo que veamos el cielo estrellado y afectando a personas, animales y al medio ambiente.")

@bot.command("Efecto")
async def efecto(ctx):
    await ctx.send("La contaminación lumínica puede alterar nuestro sueño, especialmente si hay luces que se filtran por ventanas o pantallas encendidas por la noche. También aumenta el gasto de luz y dinero, porque usamos energía que no necesitamos. Además, afecta a la fauna (como insectos, aves o murciélagos), y nos hace perder el contacto con la naturaleza: muchas personas ya no pueden ver la Vía Láctea desde sus casas.")

@bot.command("MiNivel")
async def MiNivel(ctx,*,mensaje:str):
    
    mensaje = mensaje
    
    if mensaje in luminosidad_estados:
        await ctx.send(f'Nivel de contaminación lumínica en {mensaje}: {luminosidad_estados[mensaje]}')
    else:
        await ctx.send("Err0r")
    

token = ""

bot.run(token)