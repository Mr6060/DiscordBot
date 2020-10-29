import discord
from discord.ext import commands

import db


client = commands.Bot(command_prefix=db.prefix.get_prefix)
client.remove_command("help")

