from http import client
import os
from urllib import response
from urllib.request import urlopen
from discord.ext import commands
import re

from dotenv import load_dotenv
load_dotenv('.env')

client = commands.Bot(command_prefix='$')

global item_num
item_num = 0

@client.command()
async def ping(ctx):
    await ctx.send('https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/A_small_cup_of_coffee.JPG/1200px-A_small_cup_of_coffee.JPG')

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

@client.command()
async def img(ctx, arg):
    url = "https://serpapi.com/search.json?engine=google&q="+arg+"&google_domain=google.com&gl=us&hl=en&tbm=isch&api_key=e943bb910496b0c2f927da2a95bc84819d19c75b8811a84d6375792693177796"
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    response = urlopen(url)
    #data_json = json.loads(response.read())
    data_json = response.read()
    #print(data_json)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    #IMG_REG = '(images_results\": )(\[((.*)([\n\t]))*\])'
    IMG_REG = r"thumbnail\": \"(https:.+?)\""
    matches = re.findall(IMG_REG, str(data_json))
    for match in matches:
        print(match)
    
    for i in range(item_num, item_num+5):
        await ctx.send(matches[i])

@client.command()
async def group_img(ctx, arg):
    url = "https://serpapi.com/search.json?engine=google&q="+arg+"&google_domain=google.com&gl=us&hl=en&tbm=isch&api_key=e943bb910496b0c2f927da2a95bc84819d19c75b8811a84d6375792693177796"
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    response = urlopen(url)
    #data_json = json.loads(response.read())
    data_json = response.read()
    #print(data_json)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    #IMG_REG = '(images_results\": )(\[((.*)([\n\t]))*\])'
    IMG_REG = r"thumbnail\": \"(https:.+?)\""
    matches = re.findall(IMG_REG, str(data_json))
    for match in matches:
        print(match)
    
    for i in range(item_num, item_num+5):
        await ctx.send(matches[i])
    

client.run(os.getenv('TOKEN'))