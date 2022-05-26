# bot.py
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from urllib import parse, request
import json
import asyncio
import re
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
async def pages(ctx, arg):
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
    for x in data["data"]:
        contents.append(x['embed_url'])


    pages = len(contents)
    embed=discord.Embed(title="Help page", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
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
                embed.set_image(url=contents[cur_page-1])
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




@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

bot.run(os.getenv('TOKEN'))
