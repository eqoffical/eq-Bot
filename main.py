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
'''
# Music-bot Part
ytdl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('play'):
        url = message.content.split(' ')[1]
        voice_channel = message.author.voice.channel

        try:
            voice_client = await voice_channel.connect()
        except discord.errors.ClientException:
            voice_client = message.guild.voice_client

        with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
            info = ytdl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            voice_client.stop()
            voice_client.play(discord.FFmpegPCMAudio(url2))

    if message.content.lower().startswith('stop'):
        voice_client = message.guild.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.stop()
            await voice_client.disconnect()
'''

client.run(token)
