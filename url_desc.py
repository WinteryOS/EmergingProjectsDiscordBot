from serpapi import GoogleSearch
import discord

client = discord.Client()
search_term = ""

params = {
    "q": search_term,
    "hl": "en",
    "gl": "us",
    "api_key": "c0e876ed96a74081c2761bf2fb3afd36986176c4d8ff6c9dfab6f6ebaf7d2ded"
}

search = GoogleSearch(params)
results = search.get_dict()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$search'):
        await message.channel.send('What would you like to search?')

        while True:
            user_input = client.wait_for('message')
            if user_input.author == message.author:
                search_term.this = user_input.content

    for organic_results in results.get("organic_results", []):
        position = organic_results.get("position", None)
        title = organic_results.get("title", "")
        snippet = organic_results.get("snippet", "")

        await message.channel.send(f"Position: {position}\nTitle: {title}\nSnippet: {snippet}\n\n")