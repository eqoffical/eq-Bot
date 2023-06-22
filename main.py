import discord
import random
import config
import youtube_dl
import asyncio

token = config.TOKEN

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    
    if message.author == client.user:
        return

    if message.channel.name == 'bot-spam':
        if user_message.lower() == 'hello':
    
            await message.channel.send(f'Hello {username} 👋')
        
        elif user_message.lower() == 'ping':
    
            await message.channel.send(f'Pong {username}!! 🏓')
        
        elif user_message.lower().startswith('!rnumber'):
            try:
                limit = user_message.split(' ')[1] 

                try:
                    limit = int(limit)
            
                    if limit <= 0:
                        response = "Number must be positive 🥺"
            
                    else:
                        response = f"Let it be: {random.randint(1, limit)} 🎲"
            
                except ValueError:
                    response = "I dunno bruh 🤨"
            
                await message.channel.send(response)
        
            except:
                response = f"Uhm, let it be: {random.randint(1_000_000, 9_999999)}, hope it's good for you 👀"
    
                await message.channel.send(response)
                return

client.run(token)
