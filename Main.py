# bot.py
import os
import discord
from serpapi import GoogleSearch

from dotenv import load_dotenv
load_dotenv('.env')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$Are you a robot Goigle'):
        await message.channel.send('Heavens no, I\'m the real deal')

@client.command()
async def foo(ctx, arg):
    await ctx.send(arg)

keywords = [
  "Coffee",
  "Twitter"
]

#search = requests.get('https://serpapi.com/search.json?engine=google&q=' + keywords + '&location=Salt+Lake+City%2C+Utah%2C+United+States&google_domain=google.com&gl=us&hl=en&api_key=' + api_Key)

search = GoogleSearch({"api_key": os.getenv("SERPAPI_KEY")})
# data = response_API.text
# parse_json = json.loads(data)
# link = parse_json['organic_results']['']['link']

for keyword in keywords:
  search.params_dict['q'] = keyword
  result = search.get_dict()

  print(f"Top 5 results for '{keyword}':")

  for organic_results in result.get("organic_results", [])[:5]:
    position = organic_results.get("position", None)
    title = organic_results.get("title", "")
    link = organic_results.get("link", "")

    print(f"Title: {title}\nPosition: {position}\nLink: {link}\n\n")

client.run(os.getenv('TOKEN'))