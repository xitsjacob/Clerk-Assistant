import sys

import discord
from discord.ext import commands

sys.path.insert(1, "./components/")

from rover import RoverAPI


class Ping(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("Ping cog loaded")

  @commands.hybrid_command(name="ping", description="Check the bot's latency")
  async def ping(self, ctx: commands.Context):
    bot_latency = round(self.client.latency * 1000)
    await ctx.send(f"Pong! {bot_latency} ms.", ephemeral=True)

  @commands.command(name="test")
  async def test(self, ctx: commands.Context):
    rblx = Roblox()
    roleGrabber = await rblx.congressRoleGrabber(guildID=13931602, userID=ctx.author.id)
    await ctx.send(f"Returned: {roleGrabber}")

async def setup(client: commands.Bot):
  await client.add_cog(Ping(client))
