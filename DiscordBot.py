import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
token = 'Njc3NTM0ODg3NjUzNDA4Nzk4.XkVptg._FUf8n6tNNc2nw6j_QgXLfUlLFs'

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == "Les Garcons", bot.guilds)


    print(f'{bot.user} has joined the battle!')
    print(f'{guild} is the joined guild')

@bot.event
async def on_member_update(before, after):
    await after.create_dm()
    await after.dm_channel.send("hehe nice try libtard, reported to Riot Games")
    await after.guild.text_channels[0].send("INTRUDER ALERT! Red Spy is in the base!")

@bot.event
async def on_member_join(member):
    memberMsg = ""
    await member.create_dm()
    if (str(member[:-5]) == "supersonic64"):
        memberMsg = "Eh ben bonjour mon ami, tu es le cleanest yasuo dans NA mon ami xD"
    elif (str(member[:-5]) == "DWT"):
        memberMsg = "Programmed the bot to kick you next time you ks (JAY KAY)"
    elif (str(member[:-5]) == "MattManGagnon"):
        memberMsg = "Yo the OG terraria gangsta has appeared, we boutta pop OFF"
    elif (str(member[:-5]) == "MrBlueBossMan"):
        memberMsg = "Good project for u to learn Python buddy"
    elif (str(member[:-5]) == "KillMeNow"):
        memberMsg = "STEPAHODOADOPDOPALIS why u always offline bro bb come bacc ):"
    else:
        memberMsg = "c'est un message default mon ami, cela c'est trop triste )':"
    await member.dm_channel.send(memberMsg)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    yasuo_msgs = [
        "talking about the cleanest champion in league, eh?",
        "Why can Yasuo unlock any door?",
        "Boutta E-Q flash - oh shit I missed",
        "Face the wind, but watch your b a c k"
    ]

    trash_msgs = [
        "impossible, everyone in this channel is too CLEAN",
        "aha get foked",
        "Probably just Riot not balancing their champions, as per usual"
    ]

    give_reccomendation = [
        "League of Legends (lol naw jk)",
        "Risk of Rain 2",
        "Terraria",
        "Heroes of the storm (cho gall only)",
        "golfing with friends?"
    ]

    clean_meme = [
        "Wait are we talking about Carl's Yi?",
        "Ah, discussing Matt's Thresh I see",
        "Oh, definitely not talking about Deacon then",
        "Oh look, the one thing Raymond's yasuo will never be"
    ]

    response = ""
    if "yasuo" in message.content.lower():
        response = random.choice(yasuo_msgs)
    elif "trash" in message.content.lower():
        response = random.choice(trash_msgs)
    elif "slackbot reccomend" in message.content.lower():
        response = random.choice(give_reccomendation)
    elif "clean" in message.content.lower():
        response = random.choice(clean_meme)
    elif message.content == 'raise-exception':
        response = "oh no i boutta error out foo R I P"
    await message.channel.send(response)

bot.run(token)