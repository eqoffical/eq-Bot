import discord
import random
import config

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
            await message.channel.send(f'Pong!! {username} 🏓')
        elif user_message.lower() == '!rnumber':
            response = f'Kinda {random.randrange(100)} 🤔'
            await message.channel.send(response)
            return

client.run(token)
