import discord
import random
import config
import asyncio

token = config.TOKEN
chat = config.CHAT

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

    if message.channel.name == chat:
        
# Hello

        if user_message.lower() == 'hello':
    
            await message.channel.send(f'Hello {username} 👋')
        
# Ping 

        elif user_message.lower() == 'ping':
    
            await message.channel.send(f'Pong {username}!! 🏓')
        
# Generate Random Number

        elif user_message.lower().startswith('rnumber'):
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
                response = f"Uhm, let it be: {random.randint(1_000_000, 9_999_999)}, hope it's good for you 👀"
    
                await message.channel.send(response)
                return

# Roles

        elif user_message.lower() == '!roles':
            role_list = ["💰 GTA V", "💠 Genshin Impact", "🚀 Among us", "💀 Fortnite", "🕹 Roblox", "🚗 Rocket League", "😱 Phasmophobia", "🌳 Terraria", "⛏ Minecraft", "🎯 CS:GO", "🍖 Don't Starve Together", "🏎 Forza Horizon 4"]

            # Create a formatted message with the role options
            roles_message = "Все доступные роли:\n"
            for role_name in role_list:
                roles_message += f"{role_name}\n"

            sent_message = await message.channel.send(roles_message)

        elif user_message.lower() in ["💰", "💠", "🚀", "💀", "🕹", "🚗", "😱", "🌳", "⛏", "🎯", "🍖", "🏎"]:
            role_emojis = ["💰", "💠", "🚀", "💀", "🕹", "🚗", "😱", "🌳", "⛏", "🎯", "🍖", "🏎"]
            role_index = role_emojis.index(user_message)
            role_list = ["GTA V", "Genshin Impact", "Among us", "Fortnite", "Roblox", "Rocket League", "Phasmophobia", "Terraria", "Minecraft", "CS:GO", "Don't Starve Together", "Forza Horizon 4"]

            if role_index >= 0 and role_index < len(role_list):
                role_name = role_list[role_index]
                guild = message.guild

                # Find the role object by name
                role = discord.utils.get(guild.roles, name=role_name)

                if role:
                    # Check if the user already has the role
                    if role in message.author.roles:
                        await message.author.remove_roles(role, reason="Распределение ролей")
                        await message.channel.send(f"{username}, вы больше НЕ имеете роль: {role_name} {role_emojis[role_index]}")
                    else:
                        try:
                            # Remove all other roles from the user
                            await message.author.remove_roles(*message.author.roles, reason="Распределение ролей")
                        except discord.errors.Forbidden:
                            # Ignore the error if the bot lacks permission to manage roles
                            pass
                        except discord.errors.HTTPException:
                            # Ignore the error if the role doesn't exist or is not assignable
                            pass

                        # Assign the selected role to the user
                        await message.author.add_roles(role)
                        await message.channel.send(f"Поздравляю {username}! Теперь у вас есть роль: {role_name} {role_emojis[role_index]}")
                else:
                    await message.channel.send("Какая-то ошибка, попробуйте ещё раз 🤓")

client.run(token)
