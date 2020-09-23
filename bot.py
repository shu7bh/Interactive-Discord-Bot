import discord
from discord.ext import commands
import random
import os

bot = commands.Bot(command_prefix = '.') 

@bot.event
async def on_command_error(ctx,error):
    'This is to catch all possible errors'


    await ctx.send(random.choice(open("Resource/errorResponses.txt", "r").readlines()))

@bot.event
async def on_ready():
    'Just to show that the bot is online and functioning'

    print ('Bot is ready')


for fileName in os.listdir('./Cogs'):
    if fileName.endswith('.py'):
        bot.load_extension(f'Cogs.{fileName[:-3]}')

bot.run(open('Resource/token.txt', 'r').readline())