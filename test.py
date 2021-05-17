import discord
import logging
from discord import member
from discord.ext import commands
from discord.role import RoleTags
import discord.ext.commands
import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    async def on_message(message):
     if message.author == client.user:
        return

async def on_message(message):
        print('Message from {0.author}: {0.content}'.format(message))

@client.event
async def on_message(message):

    if message.content.upper().startswith('!PING'):
      userID = message.author.id
      await message.channel.send(message.channel, "<@%s> Pong!" % (userID))
      await client.delete_message(message)

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client.run(config.TOKEN)