import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import json
import random
import youtube_dl
from pytube import YouTube

#If anyone wants to use my code, please ask me on IG: kimmuie_ , for permission.
f = open("Token.txt", "r")
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
    
@client.command(aliases=['prefix', 'Pr', 'pr', 'Pre', 'pre','Pref','pref','Prefi','prefi'])
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

@client.command(aliases=['join', 'Jo', 'jo', 'Joi', 'joi'])
async def Join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        voice_client = ctx.guild.voice_client
        if voice_client:
            connect = json_data.get('2connect1', []) if mode == "rude" else json_data.get('2connect2', [])
            random_connect = random.choice(connect)
            await ctx.channel.send(random_connect)
        else:
            await channel.connect()
            connect = json_data.get('1connect1', []) if mode == "rude" else json_data.get('1connect2', [])
            random_connect = random.choice(connect)
            await ctx.channel.send(random_connect)
    else:
        connect = json_data.get('3connect1', []) if mode == "rude" else json_data.get('3connect2', [])
        random_connect = random.choice(connect)
        await ctx.channel.send(random_connect)

@client.command(aliases=['leave', 'Le', 'le', 'Lea', 'lea','Leav','leav'])
async def Leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        connect = json_data.get('1disconnect1', []) if mode == "rude" else json_data.get('1disconnect2', [])
        random_connect = random.choice(connect)
        await ctx.channel.send(random_connect)
    else:
        connect = json_data.get('2disconnect1', []) if mode == "rude" else json_data.get('2disconnect2', [])
        random_connect = random.choice(connect)
        await ctx.channel.send(random_connect)

mute_message = False
mute_reaction = False

@client.command(aliases=['mute', 'Mu', 'mu', 'Mut', 'mut'])
async def Mute(ctx, mute_type: str = ''):
    global mute_message
    global mute_reaction
    if mute_type.lower() == 'message' or mute_type.lower() == 'm':
        mute_message = True
        await ctx.send("Botmuie has muted the message.")
    elif mute_type.lower() == 'reaction' or mute_type.lower() == 'r':
        mute_reaction = True
        await ctx.send("Botmuie has muted the reaction.")
    elif mute_type.lower() == 'both' or mute_type.lower() == 'b':
        mute_message = True
        mute_reaction = True
        await ctx.send("Botmuie has muted both message and reaction.")
    elif mute_type.lower() == '':
        class MuteView(nextcord.ui.View):
            def __init__(self):
                super().__init__()

            @nextcord.ui.button(label="Message", style=nextcord.ButtonStyle.red)
            async def message_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global mute_message
                mute_message = True
                await interaction.response.send_message("Botmuie has muted the message.")
                self.stop()

            @nextcord.ui.button(label="Reaction", style=nextcord.ButtonStyle.red)
            async def reaction_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global mute_reaction
                mute_reaction = True
                await interaction.response.send_message("Botmuie has muted the reaction.")
                self.stop()
            
            @nextcord.ui.button(label="Both", style=nextcord.ButtonStyle.grey)
            async def both_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global mute_message
                global mute_reaction
                mute_message = True
                mute_reaction = True
                await interaction.response.send_message("Botmuie has muted both message and reaction.")
                self.stop()

        await ctx.send("Please select a type to mute for Botmuie:", view=MuteView())
    else:
        await ctx.send("Invalid mute type. Please specify either 'message' or 'reaction' or 'both'.")

@client.command(aliases=['unmute', 'Un', 'un', 'Unm', 'unm','Unmu','unmu','Unmut','unmut'])
async def Unmute(ctx, mute_type: str = ''):
    global mute_message
    global mute_reaction
    if mute_type.lower() == 'message' or mute_type.lower() == 'm':
        mute_message = False
        await ctx.send("Botmuie has unmuted the message.")
    elif mute_type.lower() == 'reaction' or mute_type.lower() == 'r':
        mute_reaction = False
        await ctx.send("Botmuie has unmuted the reaction.")
    elif mute_type.lower() == 'both' or mute_type.lower() == 'b':
        mute_message = False
        mute_reaction = False
        await ctx.send("Botmuie has unmuted both message and reaction.")
    elif mute_type.lower() == '':
        class UnmuteView(nextcord.ui.View):
            def __init__(self):
                super().__init__()

            @nextcord.ui.button(label="Message", style=nextcord.ButtonStyle.green)
            async def message_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global mute_message
                mute_message = False
                await interaction.response.send_message("Botmuie has unmuted the message.")
                self.stop()

            @nextcord.ui.button(label="Reaction", style=nextcord.ButtonStyle.green)
            async def reaction_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global mute_reaction
                mute_reaction = False
                await interaction.response.send_message("Botmuie has unmuted the reaction.")
                self.stop()
            
            @nextcord.ui.button(label="Both", style=nextcord.ButtonStyle.grey)
            async def both_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global mute_message
                global mute_reaction
                mute_message = False
                mute_reaction = False
                await interaction.response.send_message("Botmuie has unmuted both message and reaction.")
                self.stop()

        await ctx.send("Please select a type to unmute for Botmuie:", view=UnmuteView())
    else:
        await ctx.send("Invalid unmute type. Please specify either 'message' or 'reaction' or 'both'.")

@client.event
async def on_reaction_add(reaction, user):
    if not mute_reaction:
        channel = reaction.message.channel
        async for message in channel.history(limit=1):
            last_message = message
        if reaction.message == last_message:
            await channel.send(reaction.emoji)


@client.event
async def on_message(message):
    global prefix
    if not message.author.bot:
        if not mute_message:
            if message.content.startswith(client.command_prefix):
                await client.process_commands(message)
            elif "//" in message.content and prefix!="//":
                amnesia = json_data.get('amnesia1', []) if mode == "rude" else json_data.get('amnesia2', [])
                random_amnesia = random.choice(amnesia)
                await message.channel.send(random_amnesia)
            elif any(word in message.content for word in json_data.get('link3', [])) or any(attachment.filename.endswith(('.png', '.jpg', '.jpeg', '.gif','pdf',)) for attachment in message.attachments):
                link = json_data.get('link1', []) if mode == "rude" else json_data.get('link2', [])
                random_message = random.choice(link)
                await message.channel.send(random_message)
            elif any(word in message.content for word in json_data.get('hello3', [])):
                hello = json_data.get('hello1', []) if mode == "rude" else json_data.get('hello2', [])
                random_message = random.choice(hello)
                await message.channel.send(random_message)
            elif any(word in message.content for word in json_data.get('ask3', [])):
                ask = json_data.get('ask1', []) if mode == "rude" else json_data.get('ask2', [])
                random_message = random.choice(ask)
                await message.channel.send(random_message)
            elif any(word in message.content for word in json_data.get('look3', [])):
                look = json_data.get('look1', []) if mode == "rude" else json_data.get('look2', [])
                random_message = random.choice(look)
                await message.channel.send(random_message)
            elif any(word in message.content for word in json_data.get('know3', [])):
                know = json_data.get('know1', []) if mode == "rude" else json_data.get('know2', [])
                random_message = random.choice(know)
                await message.channel.send(random_message)
            elif any(word in message.content for word in json_data.get('provoke3', [])):
                provoke = json_data.get('provoke1', []) if mode == "rude" else json_data.get('provoke2', [])
                random_message = random.choice(provoke)
                await message.channel.send(random_message)
            elif any(word in message.content for word in json_data.get('surprise3', [])):
                surprise = json_data.get('surprise1', []) if mode == "rude" else json_data.get('surprise2', [])
                random_message = random.choice(surprise)
                await message.channel.send(random_message)
            elif any(word in message.content for word in json_data.get('okay3', [])):
                okay = json_data.get('okay1', []) if mode == "rude" else json_data.get('okay2', [])
                random_message = random.choice(okay)
                await message.channel.send(random_message)
            elif any(word in message.content for word in json_data.get('laugh3', [])):
                okay = json_data.get('laugh1', []) if mode == "rude" else json_data.get('laugh2', [])
                random_message = random.choice(okay)
                await message.channel.send(random_message)

voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best', 'verbose': True}

ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}

@client.command(aliases=['play', 'Pl' , 'pl', 'Pla', 'pla'])
async def Play(ctx, url):
    try:
        voice_client = ctx.voice_client
        if not voice_client:
            voice_client = await ctx.author.voice.channel.connect()
            voice_clients[ctx.guild.id] = voice_client

        yt = YouTube(url)
        song_url = yt.streams.filter(only_audio=True).first().url

        voice_client.play(nextcord.FFmpegPCMAudio(song_url, **ffmpeg_options))
    except Exception as err:
        print(err)

client.run(f.read())