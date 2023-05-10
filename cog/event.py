import discord
from discord.ext import commands
from classes import My_Cog
import json
import response

with open("info.json", mode = 'r', encoding='utf8') as js:
    data = json.load(js)

class Event(My_Cog):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(data['channel_welcome']))
        await channel.send(f'{member} joined !')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')
        if user_message[0] == '?':
            reply = response.get_response(user_message[1:])
            if reply!="None": await message.author.send(reply)
        else:
            reply = response.get_response(user_message)
            if reply!="None": await message.channel.send(reply)

async def setup(bot):
    await bot.add_cog(Event(bot))