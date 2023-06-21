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
            await message.channel.send(f'Pong!! {username} 🏓')
        elif user_message.lower() == '!rnumber':
            response = f'Kinda {random.randrange(100)} 🤔'
            await message.channel.send(response)
            return

# Music-bot Part


    # Check if the message author is not a bot
    if message.author.bot:
        return

    # Check if the message has a valid command
    if message.content.startswith('play'):
        command = message.content.split(' ')
        if len(command) > 1:
            url = command[1]
            voice_channel = message.author.voice.channel

            # Connect to the voice channel
            voice_client = await voice_channel.connect()

            # Download the audio from the YouTube video
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'noplaylist': True,
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']

            # Play the audio in the voice channel
            voice_client.play(discord.FFmpegPCMAudio(url2))

            # Leave the voice channel after the audio finishes playing
            def after_playing(error):
                asyncio.run_coroutine_threadsafe(voice_client.disconnect(), client.loop)

            voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
            voice_client.source.volume = 0.5  # Adjust the volume if needed
            voice_client.source.after = after_playing

    elif message.content == 'leave':
        # Check if the message is the 'leave' command
        voice_client = discord.utils.get(client.voice_clients, guild=message.guild)

        if voice_client and voice_client.is_connected():
            await voice_client.disconnect()











client.run(token)
