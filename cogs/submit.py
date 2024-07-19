import sys

import discord
from discord.ext import commands

sys.path.insert(1, "./components/")

from trello import TrelloAPI

HOUSE_CLERK_ID: int = 1202713109236678686

class Submit(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("Submit cog loaded")

  @commands.hybrid_group()
  async def submit(self, ctx: commands.Context):
    pass

  @submit.command(name="house", description="Submits a house record")
  @commands.has_role(HOUSE_CLERK_ID)
  async def submit_house(self, ctx: commands.Context, link: str, *, bill_name: str):
    try:
      trello = TrelloAPI()
      await trello.createLegislationCard(bill_name, link)
      await ctx.send(f"Submitted {bill_name} to the House of Representatives. {link}")
    except Exception as e:
      await ctx.send(f"{e}")

async def setup(client: commands.Bot):
  await client.add_cog(Submit(client))