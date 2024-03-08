import discord
import os, random
from discord.ext import commands
import requests

from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='7', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hey 7bro, Im {bot.user}, I love quidding all around')

@bot.command()
async def buck(ctx, count_buck = 5):
    await ctx.send("17bucks" * count_buck)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('fuck off it gotta be in format NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def kys(ctx, times: int, content='IM GONNA KILL MYSELF'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def meme(ctx):
    memes = random.choice(os.listdir("images"))
    with open(f'images/{memes}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def im(ctx):
    if ctx.message.attachments:
        for archi in ctx.message.attachments:
            name= archi.filename
            url = archi.url
            await archi.save(f"./{name}")
            await ctx.send(get_class (model="keras_model.h5", labels="labels.txt", image=f"./{name}"))
    else:
        await ctx.send("Olvidaste subir la imagen :(")

bot.run(GOO GOO GAA GAA)