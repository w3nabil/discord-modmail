import discord, os, json
from dotenv import load_dotenv
from datetime import datetime as dt 

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

server_id = json.load(open("config.json"))["server_id"]
mod_channel_id = json.load(open("config.json"))["mod_channel_id"]
prefix = json.load(open("config.json"))["prefix"]
mod_role_id = json.load(open("config.json"))["mod_role_id"]

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="To People!"))
    print(f'Bot {bot.user} on air!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    if isinstance(message.channel, discord.DMChannel):
        if server_id is not None:
            if mod_channel_id is not None:
                mod_channel = bot.get_channel(mod_channel_id)
                print(mod_channel)
                if mod_channel is not None:
                    embed = discord.Embed(
                        title=f"{message.author} | {dt.now().strftime('%Y-%m-%d %H:%M:%S')}", 
                        description=f"\n\n{message.content}", 
                        color=0x00ff00
                        ) 
                    await mod_channel.send(content=f"{message.author.mention} - " ,embed=embed)
                else:
                    print("mod_channel_id is invalid")
            else:
                print("mod_channel_id is not set") 
        else:
            print("server_id is not set")
            


    if message.content.startswith("reply"):
        if message.channel.id == mod_channel_id:
            if discord.utils.get(message.author.roles, id=mod_role_id) is not None:
                target = message.content.split(" ")[1]  
                user = await bot.fetch_user(int(target))
                try:
                    await user.send(' '.join(message.content.split(" ")[2:]) + f"\n -{message.author} (Behalf of the moderation team)")  
                    embed = discord.Embed(
                        title=f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}",
                        description= f"**Replied by <@{message.author.id}> To <@{target}>** \n\n - " + ' '.join(message.content.split(' ')[2:]),  
                        color=0x00ff00
                    )
                    await message.channel.send(embed=embed)
                    await message.delete()
                except discord.NotFound:
                    await message.channel.send("User not found.")
                except discord.Forbidden:
                    await message.channel.send("Bot doesn't have permission to send a message to the user.")
                except discord.HTTPException as e:
                    await message.channel.send(f"Failed to send message: {e}")

bot.run(os.getenv('BOT_TOKEN'))
