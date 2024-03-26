import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import json
import random
from pytube import YouTube
from gtts import gTTS
import asyncio
import os
from langdetect import detect

#If anyone wants to use my code, please ask me on IG: kimmuie_ , for permission.
f = open("Token.txt", "r")
intents = nextcord.Intents.default()
intents.members = True

prefix="//"
mode="rude"
voiceGender="female"
voiceVelocity=False
voiceVelocity2="slow"

client = commands.Bot(command_prefix=prefix, intents=nextcord.Intents.all()) #intents=nextcord.Intents.all()
#api = OpenAI(api_key="YOUR_OPENAI_API_KEY_HERE")
client.remove_command("help")

with open('content.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.do_not_disturb, activity=nextcord.CustomActivity(name='//help ➤ ig: kimmuie_ ')
)
    print("The Botmuie is now ready for use.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

@client.event
async def on_voice_state_update(member):
    await member.edit(deafen=True)

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
    embed.add_field(name="Voice", value=f"Change the bot accent.\nEx. {prefix}Voice , {prefix}Voice male , {prefix}Voice female , {prefix}Voice slow , {prefix}Voice fast", inline=False)
    embed.add_field(name="Play", value=f"Play the MP3 file you specify.\nEx. {prefix}Audio (link or song name)", inline=False)
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
    embed.add_field(name="Voice", value=f"Change the bot accent.\nEx. {prefix}Voice , {prefix}Voice male , {prefix}Voice female , {prefix}Voice slow , {prefix}Voice fast", inline=False)
    embed.add_field(name="Play", value=f"Play the MP3 file you specify.\nEx. {prefix}Audio (link or song name)", inline=False)
    embed.add_field(name="Mode", value=f"Change how the bot replies to messages on the channel.\nEx. {prefix}Mode , {prefix}Mode polite , {prefix}Mode rude", inline=False)
    embed.add_field(name="Mute", value=f"Prevent the bot from replying to the message.\nEx. {prefix}Mute , {prefix}Mute message , {prefix}Mute reaction", inline=False)
    embed.add_field(name="Unmute", value=f"Allow the bot to reply to the message.\nEx. {prefix}Unmute , {prefix}Unmute message , {prefix}Unmute reaction", inline=False)
    embed.set_footer(text="ig: kimmuie_")
    await interaction.response.send_message(embed=embed)

@client.slash_command(name = "info", description = "Show all Botmuie information that have been set up")
async def info(interaction: Interaction):
    prefix = await client.get_prefix(interaction.message)
    global mode
    global voiceGender
    global voiceVelocity2
    embed = nextcord.Embed(title="Botmuie Information", color=0x8d8d8d)
    embed.set_author(name="Botmuie", icon_url=client.user.avatar.url)
    embed.add_field(name="Prefix Setting", value=f"Prefix = **{prefix}**", inline=False)
    embed.add_field(name="Mode Setting", value=f"Mode = **{mode}**", inline=False)
    embed.add_field(name="Voice Setting", value=f"Gender = **{voiceGender}** (male voice function havent been used yet)\nVelocity = **{voiceVelocity2}**", inline=False)
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
            elif any(word in message.content for word in json_data.get('couple3', [])):
                couple = json_data.get('couple1', []) if mode == "rude" else json_data.get('couple2', [])
                random_message = random.choice(couple)
                await message.channel.send(random_message)           
            elif any(word in message.content for word in json_data.get('manner3', [])):
                manner = json_data.get('manner1', []) if mode == "rude" else json_data.get('manner2', [])
                random_message = random.choice(manner)
                await message.channel.send(random_message)
            elif "ไม่" in message.content:
                await message.channel.send("ใช่")            
            elif "ใช่" in message.content:
                await message.channel.send("ไม่")

voice_clients = {}
queue = []
rqqueue = []
q = -1

@client.command(aliases=['play', 'Pl', 'pl', 'Pla', 'pla'])
async def Play(ctx, *, url=None):
    try:
        if url is None:
            url = json_data.get('url1', []) if mode == "rude" else json_data.get('url2', [])
            random_message = random.choice(url)
            await ctx.send(random_message)
            return

        voice_client = ctx.voice_client
        if not voice_client:
            voice_client = await ctx.author.voice.channel.connect()
            voice_clients[ctx.guild.id] = voice_client

        yt = YouTube(url)
        queue.append(yt)
        rqqueue.append(ctx.author.mention)
        if not voice_client.is_playing():
            await play_from_queue(ctx)
    except Exception as err:
        print(err)

        
async def play_from_queue(ctx):
    global q
    q = q + 1
    yt = queue[q]
    rq = rqqueue[q]
    voice_client = ctx.voice_client
    song_url = yt.streams.get_audio_only().url
    voice_client.play(nextcord.FFmpegPCMAudio(song_url))

    video_title = yt.title
    video_url = yt.watch_url
    video_duration = yt.length
    duration_minutes = video_duration // 60
    duration_seconds = video_duration % 60

    embed = nextcord.Embed(title="Now Playing", description=f"[{video_title}]({video_url})", color=0x00b300)
    embed.set_author(name="Botmuie", icon_url=client.user.avatar.url)
    embed.add_field(name="Duration", value=f"{duration_minutes}:{duration_seconds:02d}", inline=True)
    embed.add_field(name="Requested By", value=rq, inline=True) 
    embed.add_field(name="Queue Position", value=q+2, inline=False) 
    embed.set_footer(text="ig: kimmuie_")
    await ctx.send(embed=embed)

@client.command(aliases=['next', 'Ne', 'ne', 'Nex', 'nex'])
async def Next(ctx):
    global q
    if queue[q + 1] == None:
        embed = nextcord.Embed(title="There is no next video in queue", description=f"{prefix}play (link from youtube)", color=0xe60000)
        embed.set_author(name="Botmuie", icon_url=client.user.avatar.url)
        embed.set_footer(text="ig: kimmuie_")
        await ctx.send(embed=embed)
    else:
        await play_from_queue(ctx)

@client.command(aliases=['speak', 'Sp', 'sp', 'Spe', 'spe', 'Spea', 'spea'])
async def Speak(ctx, *speech):
    global voiceGender
    global voiceVelocity
    text = " ".join(speech)
    user = ctx.message.author
    if user.voice is not None:
        try:
            vc = await user.voice.channel.connect()
        except Exception as e:
            vc = ctx.voice_client
            print(f"Error connecting to voice channel: {e}")
        
        
        language = detect(text)
        if language == 'th':
            sound = gTTS(text=text, lang="th", slow=voiceVelocity)
        else:
            sound = gTTS(text=text, lang="en", slow=voiceVelocity)
        sound.save("tts-audio.mp3")

        if vc.is_playing():
            vc.stop()

        source = await nextcord.FFmpegOpusAudio.from_probe("tts-audio.mp3", method="fallback")
        vc.play(source, after=lambda e: print("Playback finished"))
        
        await asyncio.sleep(sound)
        await vc.disconnect()
        os.remove("tts-audio.mp3")
    else:
        connect = json_data.get('3connect1', []) if mode == "rude" else json_data.get('3connect2', [])
        random_connect = random.choice(connect)
        await ctx.send(random_connect)

@client.command(aliases=['voice', 'Vo', 'vo', 'Voi', 'voi','Voic','voic'])
async def Voice(ctx, voice_type: str = ''):
    global voiceGender
    global voiceVelocity
    global voiceVelocity2
    if voice_type.lower() == 'male' or voice_type.lower() == 'm':
        voiceGender = "male"
        await ctx.send("Botmuie is using male voice.")
    elif voice_type.lower() == 'female' or voice_type.lower() == 'fe':
        voiceGender = "female"
        await ctx.send("Botmuie is using female voice.")
    elif voice_type.lower() == 'slow' or voice_type.lower() == 's':
        voiceVelocity = False
        voiceVelocity2 = "slow"
        await ctx.send("Botmuie voice velocity is slower.")
    elif voice_type.lower() == 'fast' or voice_type.lower() == 'fa':
        voiceVelocity = True
        voiceVelocity2 = "fast"
        await ctx.send("Botmuie voice velocity is faster.")
    elif voice_type.lower() == '':
        class voiceView(nextcord.ui.View):
            def __init__(self):
                super().__init__()

            @nextcord.ui.button(label="Male", style=nextcord.ButtonStyle.green)
            async def male_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global voiceGender
                voiceGender = "male"
                await interaction.response.send_message("Botmuie is using male voice.")
                self.stop()

            @nextcord.ui.button(label="Female", style=nextcord.ButtonStyle.green)
            async def female_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global voiceGender
                voiceGender = "female"
                await interaction.response.send_message("Botmuie is using female voice.")
                self.stop()
            
            @nextcord.ui.button(label="Slow", style=nextcord.ButtonStyle.blurple)
            async def slow_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global voiceVelocity
                global voiceVelocity2
                voiceVelocity = False
                voiceVelocity2 = "slow"
                await interaction.response.send_message("Botmuie voice velocity is slower.")
                self.stop()
            @nextcord.ui.button(label="Fast", style=nextcord.ButtonStyle.blurple)
            async def fast_button_callback(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
                global voiceVelocity
                global voiceVelocity2
                voiceVelocity = True
                voiceVelocity2 = "fast"
                await interaction.response.send_message("Botmuie voice velocity is faster.")
                self.stop()

        await ctx.send("Please select a voice type to set up for Botmuie:", view=voiceView())
    else:
        await ctx.send("Invalid voice type. Please specify either 'male' or 'female' or 'slow' or 'fast'.")

client.run(f.read())