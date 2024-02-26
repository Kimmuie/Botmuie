import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import json
import random

#If anyone wants to use my code, please ask me on IG: kimmuie_ , for permission.

intents = nextcord.Intents.default()
intents.members = True

prefix="//"
mode="rude"

client = commands.Bot(command_prefix=prefix, intents=nextcord.Intents.all()) #intents=nextcord.Intents.all()

client.remove_command("help")

with open('content.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.do_not_disturb, activity=nextcord.CustomActivity(name='//help ➤ ig: kimmuie_ ')
)
    print("The Botmuie is now ready for use.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

@client.command(aliases=['prefix', 'Pr', 'pr', 'Pre', 'pre'])
async def Prefix(ctx, new_prefix: str):
    global prefix 
    prefix = new_prefix
    await ctx.send(f"Prefix changed to **{new_prefix}** successfully.")
    client.command_prefix = new_prefix


@client.command(aliases=['help', 'He' , 'he', 'Hel', 'hel'])
async def Help(ctx):
    prefix = await client.get_prefix(ctx.message)
    global mode
    embed = nextcord.Embed(title="List of Commands", description=f"Now, with the prefix **{prefix}** and **{mode}** mode enabled.", color=0x8d8d8d)
    embed.set_author(name="Botmuie", icon_url=client.user.avatar.url)
    embed.add_field(name="Help", value=f"Open the list of commands along with their descriptions.\nEx. {prefix}Help", inline=False)
    embed.add_field(name="Prefix", value=f"Alter the bot's prefix.\nEx. {prefix}Prefix (new prefix)", inline=False)
    embed.add_field(name="Gate", value=f"Set the greeting and farewell messages for the channel you used.\nEx. {prefix}Gate , {prefix}Gate enter , {prefix}Gate exit", inline=False)
    embed.add_field(name="Join", value=f"Make the bot to join your current audio channel.\nEx. {prefix}Join", inline=False)
    embed.add_field(name="Leave", value=f"Make the bot to leave your current audio channel.\nEx. {prefix}Leave", inline=False)
    embed.add_field(name="Speak", value=f"Make the bot speak the message you type.\nEx. {prefix}Speak (message)", inline=False)
    embed.add_field(name="Audio", value=f"Play the MP3 file you specify.\nEx. {prefix}Audio (link or song name)", inline=False)
    embed.add_field(name="Mode", value=f"Change how the bot replies to messages on the channel.\nEx. {prefix}Mode , {prefix}Mode polite , {prefix}Mode rude", inline=False)
    embed.add_field(name="Mute", value=f"Prevent the bot from replying to the message.\nEx. {prefix}Mute , {prefix}Mute message , {prefix}Mute reaction", inline=False)
    embed.add_field(name="Unmute", value=f"Allow the bot to reply to the message.\nEx. {prefix}Unmute , {prefix}Unmute message , {prefix}Unmute reaction", inline=False)
    embed.set_footer(text="ig: kimmuie_")
    await ctx.send(embed=embed)

@client.slash_command(name = "help", description = "List of Commands")
async def help(interaction: Interaction):
    prefix = await client.get_prefix(interaction.message)
    global mode
    embed = nextcord.Embed(title="List of Commands", description=f"Now, with the prefix **{prefix}** and **{mode}** mode enabled.", color=0x8d8d8d)
    embed.set_author(name="Botmuie", icon_url=client.user.avatar.url)
    embed.add_field(name="Help", value=f"Open the list of commands along with their descriptions.\nEx. {prefix}Help", inline=False)
    embed.add_field(name="Prefix", value=f"Alter the bot's prefix.\nEx. {prefix}Prefix (new prefix)", inline=False)
    embed.add_field(name="Gate", value=f"Set the greeting and farewell messages for the channel you used.\nEx. {prefix}Gate , {prefix}Gate enter , {prefix}Gate exit", inline=False)
    embed.add_field(name="Join", value=f"Make the bot to join your current audio channel.\nEx. {prefix}Join", inline=False)
    embed.add_field(name="Leave", value=f"Make the bot to leave your current audio channel.\nEx. {prefix}Leave", inline=False)
    embed.add_field(name="Speak", value=f"Make the bot speak the message you type.\nEx. {prefix}Speak (message)", inline=False)
    embed.add_field(name="Audio", value=f"Play the MP3 file you specify.\nEx. {prefix}Audio (link or song name)", inline=False)
    embed.add_field(name="Mode", value=f"Change how the bot replies to messages on the channel.\nEx. {prefix}Mode , {prefix}Mode polite , {prefix}Mode rude", inline=False)
    embed.add_field(name="Mute", value=f"Prevent the bot from replying to the message.\nEx. {prefix}Mute , {prefix}Mute message , {prefix}Mute reaction", inline=False)
    embed.add_field(name="Unmute", value=f"Allow the bot to reply to the message.\nEx. {prefix}Unmute , {prefix}Unmute message , {prefix}Unmute reaction", inline=False)
    embed.set_footer(text="ig: kimmuie_")
    await interaction.response.send_message(embed=embed)

enter_channel = None
exit_channel = None

@client.command(aliases=['gate', 'Ga', 'ga', 'Gat', 'gat'])
async def Gate(ctx, gate_type: str = ''):
    global enter_channel
    global exit_channel
    
    if gate_type.lower() == 'enter':
        enter_channel = ctx.channel.id
        await ctx.send("This channel has become an entry gate.")
    elif gate_type.lower() == 'exit':
        exit_channel = ctx.channel.id
        await ctx.send("This channel has become an exit gate.")
    elif gate_type.lower() == '':
        class GateView(nextcord.ui.View):
            def __init__(self):
                super().__init__()

            @nextcord.ui.button(label="Entry", style=nextcord.ButtonStyle.green)
            async def enter_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global enter_channel
                enter_channel = interaction.channel.id
                await interaction.response.send_message("This channel has become an entry gate.")
                self.stop()

            @nextcord.ui.button(label="Exit", style=nextcord.ButtonStyle.red)
            async def exit_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global exit_channel
                exit_channel = interaction.channel.id
                await interaction.response.send_message("This channel has become an exit gate.")
                self.stop()

        await ctx.send("Please select a gate type for this channel:", view=GateView())
    else:
        await ctx.send("Invalid gate type. Please specify either 'enter' or 'exit'.")

@client.event
async def on_member_join(member):
    global enter_channel
    if enter_channel:
        channel = client.get_channel(enter_channel)
        await channel.send(f"Welcome {member.display_name}!")

@client.event
async def on_member_remove(member):
    global exit_channel
    if exit_channel:
        channel = client.get_channel(exit_channel)
        await channel.send(f"Goodbye {member.display_name}!")


@client.command(aliases=['mode', 'Mo', 'mo', 'Mod', 'mod'])
async def Mode(ctx, mode_type: str = ''):
    global mode
    if mode_type.lower() == 'polite':
        if mode=="rude":
            mode="polite"
            await ctx.send("Botmuie has become polite.")
        else:
            await ctx.send("Botmuie is already polite.")
    elif mode_type.lower() == 'rude':
        if mode=="rude":
            await ctx.send("Botmuie is already rude.")
        else:
            mode="rude"
            await ctx.send("Botmuie has become rude.")
    elif mode_type.lower() == '':
        class ModeView(nextcord.ui.View):
            def __init__(self):
                super().__init__()

            @nextcord.ui.button(label="Polite", style=nextcord.ButtonStyle.green)
            async def polite_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global mode
                if mode=="rude":
                    mode="polite"
                    await interaction.response.send_message("Botmuie has become polite.")
                else:
                    await interaction.response.send_message("Botmuie is already polite.")
                self.stop()
            @nextcord.ui.button(label="Rude", style=nextcord.ButtonStyle.red)
            async def rude_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global mode     
                if mode=="rude":
                    await interaction.response.send_message("Botmuie is already rude.")
                else:
                    mode="rude"
                    await interaction.response.send_message("Botmuie has become polite.")
                self.stop()
        await ctx.send("Please select a behavior for Botmuie:", view=ModeView())
    else:
        await ctx.send("Invalid behavior. Please specify either 'polite' or 'rude'.")

@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send("กำลังเข้าไป")
    else:
        await ctx.send("เข้าไปสักช่องนึงก่อนนะไอเบือก")

@client.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("ออกมาล่ะ")
    else:
        await ctx.send("กุไม่ได้อยู่แต่แรกไอตูดหมึก")
            
@client.command()
async def embed(ctx):
    embed = nextcord.Embed(title="Kuy", url="https://google.com", description="yay", color=0xcc0000)
    embed.set_author(name=ctx.author.display_name, url="https://wallpapercave.com/wp/wp3271017.png", icon_url=ctx.author.avatar.url)
    embed.set_thumbnail(url="https://preview.redd.it/ceetrhas51441.jpg?auto=webp&s=84ab80b5034f99e055f4105baa18ef7e7e0914e0")
    embed.add_field(name="time left", value="555", inline=True)
    embed.add_field(name="time left", value="555", inline=True)
    embed.set_footer(text="ig: kimmuie_")
    await ctx.send(embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    # Fetching the last message in the channel
    async for message in channel.history(limit=1):
        last_message = message

    # Checking if the reacted message is the last message in the channel
    if reaction.message == last_message:
        await channel.send(reaction.emoji)


@client.event
async def on_message(message):
    global prefix
    if not message.author.bot:
        if message.content.startswith(client.command_prefix):
            await client.process_commands(message)
        elif "//" in message.content and prefix!="//":
            amnesia = json_data.get('amnesia1', []) if mode == "rude" else json_data.get('amnesia2', [])
            random_amnesia = random.choice(amnesia)
            await message.channel.send(random_amnesia)
        elif "hi" in message.content:
            greetings = json_data.get('hello1', []) if mode == "rude" else json_data.get('hello2', [])
            random_greeting = random.choice(greetings)
            await message.channel.send(random_greeting)

client.run('MTIwODcwMDI4OTk0ODA2NTg0NQ.GXxvy1.pZQk2ac1IKGddJ-K10LZKTwz5csvE9K42DzJE0')