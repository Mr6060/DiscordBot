import discord
from discord.ext import commands

import db


client = commands.Bot(command_prefix="..")
client.remove_command("help")

with open("./token.txt", "r") as file:
    token = file.read()


client.run(token.strip())


