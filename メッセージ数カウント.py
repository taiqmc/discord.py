import discord
from discord.ext import commands
from datetime import datetime, timezone
import os

intents = discord.Intents.all()
intents.guilds = True
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("起動完了")

@bot.command()
async def count(ctx, member: discord.Member):
    today = datetime.now(timezone.utc).date()
    midnight = datetime.combine(today, datetime.min.time(), tzinfo=timezone.utc)
    count = 0
    async for message in ctx.channel.history(after=midnight):
        if message.author == member:
            count += 1
    await ctx.send(f'{member.display_name}はこのチャンネルで{count}回発言しました')

bot.run(token)
