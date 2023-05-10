import discord
from discord.ext import commands
import response, asyncio, json, os, random



with open("info.json", mode = 'r', encoding='utf8') as js:
    data = json.load(js)

intents =  discord.Intents.default()
intents.message_content = True
#client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix='!', intents = intents)

def run_bot():
    
    @bot.event
    async def on_ready():
        print(f'{bot.user} is online!')

    @bot.command()
    async def load(ctx, extension):
        await bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} loaded')
    
    @bot.command()
    async def unload(ctx, extension):
        await bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} unloaded')

    @bot.command()
    async def reload(ctx, extension):
        await bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} reloaded')

    bot.run(data['TOKEN'])

async def load_extension():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

asyncio.run(load_extension())
if __name__ == "__main__":
   run_bot()