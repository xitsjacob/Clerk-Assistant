import asyncio
import os

import discord
from discord.ext import commands

import components

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  await client.tree.sync()

async def load():
    for filename in os.listdir("./cogs/"):
        if filename.endswith(".py"):
          await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
  async with client:
    await load()
    await client.start(os.environ['BOT_TOKEN'])

asyncio.run(main())