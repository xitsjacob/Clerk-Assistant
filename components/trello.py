import asyncio
import json
import os

import requests

TRELLO_API_KEY: str = os.environ['TRELLO_API_KEY']
TRELLO_TOKEN: str = os.environ['TRELLO_TOKEN']

class TrelloAPI():
  def __init__(self):
    pass

  async def createLegislationCard(self, billName: str, billLink: str):
    
    url = "https://api.trello.com/1/cards"

    headers = {
      'Accept': 'application/json',
    }
    
    congressQuery = {
      'name': billName,
      'urlSource': billLink,

      # Required
      'idList': "62eb0dd1839d1182f4be8ea8",
      'key': TRELLO_API_KEY,
      'token': TRELLO_TOKEN,
    }

    houseQuery = {
      'name': billName,
      'urlSource': billLink,

      # Required
      'idList': "64d7b7133bc84bd9be79938d",
      'key': TRELLO_API_KEY,
      'token': TRELLO_TOKEN,
    }

    try:
      response1 = requests.request(
        "POST",
        url,
        headers=headers,
        params=congressQuery,
      )

      response2 = requests.request(
        "POST",
        url,
        headers=headers,
        params=houseQuery,
      )

      return response1 and response2

    except requests.exceptions.RequestException as e:
      print(f'Error accessing Trello API: {e}')
      return False