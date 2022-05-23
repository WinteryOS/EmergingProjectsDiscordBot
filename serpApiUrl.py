from ast import keyword
import os
import requests
import discord
from serpapi import GoogleSearch
import json

# @Client.command()
# async def foo(ctx, arg):
#     await ctx.send(arg)

#SERPAPI_KEY = "9a44608178a3b7ad9888bb12ed05a1992916835b8af2d5bc1fc164a5f8b1201d";
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


# params = {
#     "q": "Coffee",
#     "api_key": "9a44608178a3b7ad9888bb12ed05a1992916835b8af2d5bc1fc164a5f8b1201d",
#     "engine": "google",
#     "google_domain": "google.com",
#     "gl": "us",
#     "hl": "en"
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# print(results);