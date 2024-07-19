import os

import requests
from roblox import Client

ROVER_API_KEY = os.environ['ROVER_API_KEY']

client = Client()
GROUP_ID: int = 13931602

class RoverAPI():
  def __init__(self):
    pass

  async def congressRoleGrabber(self, guildID, userID):

    url = "https://registry.rover.link/api/" + f"guilds/{guildID}/discord-to-roblox/{userID}"
    headers = {
      'Authorization': f'Bearer {ROVER_API_KEY}',
      # 'Content-Type': 'application/json',
    }

    try:
      res = requests.get(url, headers=headers)
      res.raise_for_status() # Raise an exception for HTTP errors

      data = res.json()
    
      congressRole = await client.get_group(GROUP_ID)
      congressRoleMembers = congressRole.get_member(data['robloxId'])
      if congressRoleMembers:
        print(congressRoleMembers)
        return True
      else:
        print(congressRoleMembers)
        return False
        
    except requests.exceptions.RequestException as e:
      print(f'Error accessing ROVER API: {e}')
      return False