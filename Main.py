# bot.py
import os
import discord

from dotenv import load_dotenv
load_dotenv('.env')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$Are you a robot Goigle'):
        await message.channel.send('Heavens no, I\'m the real deal')

client.run(os.getenv('TOKEN'))