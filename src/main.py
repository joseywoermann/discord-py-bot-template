import discord
from discord.ext import commands, tasks
import json, os, logging


# Load the token and prefix | This JSON file should be in a .gitignore
with open('config.json','r') as file:
    config = json.load(file)

# Create a new bot (client) with the token & prefix specified in the JSON
client = commands.bot(
    command_prefix = config.prefix,
    intents = discord.intents.all()
)

# Remove the default help command
client.remove_command("help")


# Signify that the bot is online
@client.event
async def on_ready():
    logging.info("Ready!")


# Load all extensions (commands/cogs)
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        client.load_extension(f"commands.{filename[:-3]}")


client.run(config.token)