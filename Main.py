# bot.py
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from urllib import parse, request
import json
import asyncio
import re
from serpapi import GoogleSearch
from urllib.request import urlopen

bot = Bot("$")

from dotenv import load_dotenv
load_dotenv('.env')

client = commands.Bot(command_prefix="$")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if message.content.startswith( prefix + 'Are you a robot Goigle'):
#         await message.channel.send('Heavens no, I\'m the real deal')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def url(ctx, arg):
    await ctx.send(arg)

    search = GoogleSearch({"api_key": "9a44608178a3b7ad9888bb12ed05a1992916835b8af2d5bc1fc164a5f8b1201d"})  

    results = []
    search.params_dict['q'] = arg
 
    result = search.get_dict()

    cur_page = 1
    contents = []

    print(f"Top 5 results for '{arg}':")
 
    for organic_results in result.get("organic_results", [])[:5]:
        position = organic_results.get("position", None)
        title = organic_results.get("title", "")
        link = organic_results.get("link", "")
        # formattedStr = f"Title: {title} \nPosition: {position} \nLink: {link}"
        # results.append(formattedStr)
        
        # await ctx.send(f"Title: {title}\nPosition: {position}\nLink: {link}")

        desc = f"\nTitle: {title}\Link: {link}\n\n"

        contents.append(desc)
        print(contents)

    pages = len(contents)
    embed=discord.Embed(title="URL results", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text="footer")
    message = await ctx.send(embed=embed)

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    print(ctx.author)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                new_embed=discord.Embed(title="URL results", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
                new_embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
                new_embed.set_footer(text="footer")
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                new_embed=discord.Embed(title="URL results", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
                new_embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
                new_embed.set_footer(text="footer")
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await message.delete()
            break
    
@bot.command()
async def img(ctx, arg):
    global item_num
    item_num = 0
    url = "https://serpapi.com/search.json?engine=google&q="+arg+"&google_domain=google.com&gl=us&hl=en&tbm=isch&api_key=e943bb910496b0c2f927da2a95bc84819d19c75b8811a84d6375792693177796"
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    response = urlopen(url)
    #data_json = json.loads(response.read())
    data_json = response.read()
    #print(data_json)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    IMG_REG = r"thumbnail\": \"(https:.+?)\""
    matches = re.findall(IMG_REG, str(data_json))
    for match in matches:
        print(match)
        five_items = ""
    for i in range(item_num+5, item_num+10):
        five_items += matches[i] + "\n"
        #await ctx.send(matches[i])
    await ctx.send(five_items)
    #five_items = ""
    item_num = item_num + 5

@bot.command()
async def img_page(ctx, arg):
    cur_page = 1

    global item_num
    item_num = 0
    url = "https://serpapi.com/search.json?engine=google&q="+arg+"&google_domain=google.com&gl=us&hl=en&tbm=isch&api_key=e943bb910496b0c2f927da2a95bc84819d19c75b8811a84d6375792693177796"
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    response = urlopen(url)
    #data_json = json.loads(response.read())
    data_json = response.read()
    #print(data_json)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    IMG_REG = r"thumbnail\": \"(https:.+?)\""
    contents = re.findall(IMG_REG, str(data_json))

    print(contents)
    pages = len(contents)
    embed=discord.Embed(title="Help page", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
    embed.set_image(url=contents[0])
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text="footer")
    message = await ctx.send(embed=embed)
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    print(ctx.author)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                new_embed=discord.Embed(title="Help page", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
                new_embed.set_image(url=contents[cur_page-1])
                print(contents[cur_page-1])
                new_embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
                new_embed.set_footer(text="footer")
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                new_embed=discord.Embed(title="Help page", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
                new_embed.set_image(url=contents[cur_page-1])
                new_embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
                new_embed.set_footer(text="footer")
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending 

@bot.command()
async def giphy(ctx, arg):
    cur_page = 1

    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({
        "q": arg,
        "api_key": "E4ZP12SKQWFZl4VKhlpkOJc26LSi2eyb",
        "limit": "5"
    })

    contents = []
    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
    for z in range(0,5):
        contents.append(data['data'][z]['images']['original']['url'])
        print(data['data'][z]['images']['original']['url'])

    print(contents)
    pages = len(contents)
    embed=discord.Embed(title="Help page", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
    embed.set_image(url=contents[0])
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text="footer")
    message = await ctx.send(embed=embed)
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    print(ctx.author)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                new_embed=discord.Embed(title="Help page", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
                new_embed.set_image(url=contents[cur_page-1])
                print(contents[cur_page-1])
                new_embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
                new_embed.set_footer(text="footer")
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                new_embed=discord.Embed(title="Help page", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
                new_embed.set_image(url=contents[cur_page-1])
                new_embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
                new_embed.set_footer(text="footer")
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending 

@bot.command()
async def search(ctx, arg):
    await ctx.send(arg)

    params = {
    "q": arg,
    "hl": "en",
    "gl": "us",
    "api_key": "c0e876ed96a74081c2761bf2fb3afd36986176c4d8ff6c9dfab6f6ebaf7d2ded"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    cur_page = 1
    contents = []
    
    for organic_results in results.get("organic_results", [])[:5]:
        position = organic_results.get("position", None)
        title = organic_results.get("title", "")
        snippet = organic_results.get("snippet", "")

        # await ctx.channel.send(f"Result #{position}:\nTitle: {title}\nSnippet: {snippet}\n\n")

        desc = f"\nTitle: {title}\nSnippet: {snippet}\n\n"

        contents.append(desc)
        print(contents)

    pages = len(contents)
    embed=discord.Embed(title="Search results", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text="footer")
    message = await ctx.send(embed=embed)

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    print(ctx.author)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                new_embed=discord.Embed(title="Search results", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
                new_embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
                new_embed.set_footer(text="footer")
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                new_embed=discord.Embed(title="Search results", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
                new_embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
                new_embed.set_footer(text="footer")
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await message.delete()
            break

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

bot.run(os.getenv('TOKEN'))
