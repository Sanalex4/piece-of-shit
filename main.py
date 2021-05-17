import discord
import logging
from discord import channel
import discord.ext.commands
import config
import asyncio

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
    if message.author == client.user:
        return 

    if message.content.startswith('Ку'):
        message = await message.channel.send('С кем ты блять здороваешься долбаёбина?')
        await asyncio.sleep(1)  # this is so the message has time to be read
        await message.edit(content="Ой! Что?")
    if message.content.startswith('А да'):
        message = await message.channel.send('Ну да')
    if message.author == client.user:
        return    
    if message.content.startswith('Ну да'):
            await message.channel.send('А да')

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client.run(config.TOKEN)