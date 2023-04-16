import requests, json
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix="$")


@bot.event
async def on_ready():
    print("Бот готов к работе.")
    # for guild in bot.guilds:
    #     for channel in guild.text_channels:
    #         print(channel)
    #         await channel.send(f"Бот готов к работе. ")


@commands.has_permissions(kick_members=True, administrator=True)
@bot.command(name="kick")
async def _kick(ctx, member: discord.Member, *, reason="Причина не указана"):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)


@bot.command(name="film")  # $film название
async def _film(ctx, *, arg):
    response = requests.get("http://www.omdbapi.com/?t=" + arg + "&apikey=617499c0")
    r = response.json()
    temp = "Название: " + r["Title"] + "\n"
    temp += "Год выхода: " + str(r["Year"]) + "\n"
    temp += "Длительность: " + r["Runtime"] + "\n"
    temp += "Жанр: " + r["Genre"] + "\n"
    await ctx.send(temp)
    img_data = requests.get(r["Poster"]).content
    with open("image_name.jpg", "wb") as h:
        h.write(img_data)
    await ctx.send(file=discord.File("image_name.jpg"))


bot.run("MTA3NzIyNzYwMzMyMjIyODc0Ng.GFCdun.Jv-LmY58gkJRD2Nz9340K1ovexGw3XI0ZtRm5g")


