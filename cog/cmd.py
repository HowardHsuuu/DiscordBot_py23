import discord
from discord.ext import commands
from classes import My_Cog

class Cmd(My_Cog):
    @commands.command()
    async def hi(self, ctx):
        await ctx.send("hello")
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

async def setup(bot):
    await bot.add_cog(Cmd(bot))