# bot.py
import os
import discord
from serpapi import GoogleSearch

from dotenv import load_dotenv
load_dotenv('.env')

client = discord.Client()
# bot = commands.Bot(command_prefix='$')
bot = Bot("$")
search_term = ""

params = {
    "q": search_term,
    "hl": "en",
    "gl": "us",
    "api_key": "c0e876ed96a74081c2761bf2fb3afd36986176c4d8ff6c9dfab6f6ebaf7d2ded"
}

search = GoogleSearch(params)
results = search.get_dict()

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if message.content.startswith('$Are you a robot Goigle'):
#         await message.channel.send('Heavens no, I\'m the real deal')

@bot.command()
async def search(ctx, arg):
    await ctx.send(arg)

    if ctx.author == client.user:
        return
    
    user_input = ctx.arg
    if user_input.author == ctx.author:
        search_term.this == user_input.content

    for organic_results in results.get("organic_results", []):
        position = organic_results.get("position", None)
        title = organic_results.get("title", "")
        snippet = organic_results.get("snippet", "")

        await ctx.channel.send(f"Position: {position}\nTitle: {title}\nSnippet: {snippet}\n\n")

client.run(os.getenv('TOKEN'))