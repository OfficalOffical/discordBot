import discord

from discord.ext import commands
import pandas as pd
import requests
import io
import re
from datetime import datetime


import writeToDrive

# Replace 'YOUR_BOT_TOKEN' with the token you copied from the Discord Developer Portal.
BOT_TOKEN = ''

# Define the command prefix (e.g., "!hello")
command_prefix = "!"

# This example requires the 'message_content' intent.
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=command_prefix, intents=intents)



def extract_text_after_second_hyphen(text):
    result = re.search(r'^(?:[^-]*-){2}(.*)', text)
    if result:
        return result.group(1)
    else:
        return None


# Function to read the CSV file from a public Google Drive link
def read_google_drive_csv(link):
    response = requests.get(link)
    content = response.content
    return pd.read_csv(io.StringIO(content.decode('utf-8')),delimiter='\t')

# Publicly accessible Google Drive link to the CSV file
csv_file_link = ''  # Replace this with the actual link

# Load the CSV file into a pandas DataFrame
df = read_google_drive_csv(csv_file_link)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="drive")
async def drive(ctx, time_spend: str, description: str):
    #sherpaName = ctx.user.name
    sherpaName = ctx.user.global_name
    channelName = ctx.channel.name
    sherpalingName = extract_text_after_second_hyphen(channelName)

    dummyTicketTranscript = "12391293"
    if sherpalingName == None:
        print("Problem")

    whenHelped = datetime.utcnow().strftime('%Y-%m-%d')

    print(whenHelped)

    writeToDrive.write_to_google_sheet(sherpaName,whenHelped,sherpalingName,time_spend,description,dummyTicketTranscript)










bot.run(BOT_TOKEN)






