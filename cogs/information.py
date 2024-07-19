from typing import Literal, Optional

import discord
from discord.ext import commands

trelloBoards = {
  "NARA Hub": "https://trello.com/b/iPS4zVCc/nara-hub",
  "Public Law Database": "https://trello.com/b/ynFi49qG/public-law-database",
  "Presidential Archives": "https://trello.com/b/aXTOEhZr/presidential-archives",
  "Congress": "https://trello.com/b/7H03kZdb/united-states-congress",
  "House of Represenattives": "https://trello.com/b/ewKLnTtA/usa-house-records",
  "Senate": "https://trello.com/b/XMzm73zO/usa-senate-records",
  "D.C. City Council": "https://trello.com/b/UqL8oQbO/district-of-columbia-city-council",
  "Federal Rules of Procedure": "https://trello.com/b/REy0E12l/federal-rules-of-procedure",
  "Supreme Court": "https://trello.com/b/cz62lo6v/supreme-court-of-the-united-states",
  "District Court": "https://trello.com/b/lqpqIObq/united-states-court",
}

class Information(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("Information cog loaded")

  @commands.hybrid_command(name="trello", description="Gives you the link to the corresponding Trello board")
  async def trello(self, ctx: commands.Context, board: Optional[Literal[tuple(trelloBoards.keys())]] = None):

    if board is None:
      trelloBoardEmbed = discord.Embed(title="Trello Boards", description=f"The following are the Trello boards for the various departments \n\n" + "\n".join(f"**[{key}]({value})**" for key, value in trelloBoards.items()), color=discord.Color.red())
    else:
      trelloBoardEmbed = discord.Embed(description=f"**[{board} Trello Board]({trelloBoards[board]})**", color=discord.Color.red())

    await ctx.send(embed=trelloBoardEmbed, ephemeral=True)
  

async def setup(client: commands.Bot):
  await client.add_cog(Information(client))