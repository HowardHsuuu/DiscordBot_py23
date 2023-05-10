import discord
from discord.ext import commands

class My_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot