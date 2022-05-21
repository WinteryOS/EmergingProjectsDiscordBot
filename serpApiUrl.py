import os
import requests
import discord
from serpapi import GoogleSearch
import json

api_Key = "9a44608178a3b7ad9888bb12ed05a1992916835b8af2d5bc1fc164a5f8b1201d";
googleSearch = "Coffee";

response_API = requests.get('https://serpapi.com/search.json?engine=google&q=' + googleSearch + '&location=Salt+Lake+City%2C+Utah%2C+United+States&google_domain=google.com&gl=us&hl=en&api_key=' + api_Key)

data = response_API.text
parse_json = json.loads(data)
link = parse_json['organic_results']['']['link']

for dict in parse_json:
  manipulate dict

print("Link", link)

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