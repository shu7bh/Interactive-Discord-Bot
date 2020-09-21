import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print ('Bot is ready')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@bot.command()
async def ping(context):
    await context.send(f'{round(bot.latency * 1000)}ms')

@bot.command(aliases = ['8ball'])
async def _8ball(context, *, q):
    res = list(open('8ballResponses.txt', 'r').readlines())
    await context.send(f'Question: {q}\nAnswer: {random.choice(res)}')

@bot.command(aliases = ['remove'])
async def clear(ctx, amt = 10):
    await ctx.channel.purge(limit=amt+1)

@bot.command()
async def selfidentify(ctx, *, name):
    await ctx.send(f'{ctx.author}, you are identified as {name}')
    
bot.run(open('token.txt', 'r').readline())