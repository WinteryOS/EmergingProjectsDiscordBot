# bot.py
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
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
async def pages(ctx):
    pages = 4
    cur_page = 1
    contents = ["This is page 1!", "This is page 2!", "This is page 3!", "This is page 4!"]
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
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                new_embed=discord.Embed(title="Help page", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
                new_embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
                new_embed.set_footer(text="footer")
                await message.edit(embed=new_embed)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                new_embed=discord.Embed(title="Help page", description=(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}"), color=0x00ffc8)
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
