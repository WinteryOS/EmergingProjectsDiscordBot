# bot.py
#from imaplib import _CommandResults
import os
from discord.ext import commands
from discord.ext.commands import Bot
import discord
from jmespath import search
from serpapi import GoogleSearch

from dotenv import load_dotenv
load_dotenv('.env')
bot = Bot("$")

bot = commands.Bot(command_prefix="$")

@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('$Are you a robot Goigle'):
        await message.channel.send('Heavens no, I\'m the real deal')

# keywords = [
#   "Coffee",
#   "Twitter"
# ]

@bot.command()
async def url(ctx, arg):
  search = GoogleSearch({"api_key": "9a44608178a3b7ad9888bb12ed05a1992916835b8af2d5bc1fc164a5f8b1201d"})  
# data = response_API.text
# parse_json = json.loads(data)
# link = parse_json['organic_results']['']['link']

#for keyword in keywords:
  # search = GoogleSearch({"api_key": os.getenv("SERPAPI_KEY")})
  results = []
  search.params_dict['q'] = arg
 
  result = search.get_dict()

  print(f"Top 5 results for '{arg}':")
 
  for organic_results in result.get("organic_results", [])[:5]:
    position = organic_results.get("position", None)
    title = organic_results.get("title", "")
    link = organic_results.get("link", "")
    #results.append(f"'''Title: {title} \nPosition: {position} \nLink: {link}'''")
    formattedStr = f"Title: {title} \nPosition: {position} \nLink: {link}"
    results.append(formattedStr)



    #print(f"Title: {title}\nPosition: {position}\nLink: {link}")

    #print(result)
    
    await ctx.send(f"Title: {title}\nPosition: {position}\nLink: {link}")
  #await ctx.channel.send(f"Title: {title}\nPosition: {position}\nLink: {link}\n\n")

#search = requests.get('https://serpapi.com/search.json?engine=google&q=' + keywords + '&location=Salt+Lake+City%2C+Utah%2C+United+States&google_domain=google.com&gl=us&hl=en&api_key=' + api_Key)

# data = response_API.text
# parse_json = json.loads(data)
# link = parse_json['organic_results']['']['link']

# for keyword in :
#   search.params_dict['q'] = keyword
#   result = search.get_dict()

#   print(f"Top 5 results for '{arg}':")

#   for organic_results in result.get("organic_results", [])[:5]:
#     position = organic_results.get("position", None)
#     title = organic_results.get("title", "")
#     link = organic_results.get("link", "")

#     print(f"Title: {title}\nPosition: {position}\nLink: {link}\n\n")

bot.run(os.getenv('TOKEN'))