import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = '.')


def selfIdentify(message,name):
    f = open("realNames.txt","a+")
    f.write(f'{message.author.id} = {name}\n')
    f.close()


async def findName(message, m):
    f = open("realNames.txt", "r+")
    f1 = f.readlines()
    for x in f1:
        arr = x.split(" = ", 1)
        if str(m.id) == arr[0]:
            await message.channel.send(arr[1])
            break


@bot.event
async def on_ready():
    'Just to show that the bot is online and functioning'
    print ('Bot is ready')

@bot.event
async def on_member_join(member):
    'To keep a track of who has entered the server'
    print(f'{member} has joined a server')

@bot.event
async def on_member_remove(member):
    'To keep a track of who has exited the server'
    print(f'{member} has left the server')

@bot.command()
async def ping(context):
    'To get the time taken by the bot to reply'
    await context.send(f'{round(bot.latency * 1000)}ms')

@bot.command(aliases = ['8ball'])
async def _8ball(context, *, q):
    'A fun section where the bot predicts answers'
    res = list(open('8ballResponses.txt', 'r').readlines())
    await context.send(f'Question: {q}\nAnswer: {random.choice(res)}')

@bot.command(aliases = ['remove'])
async def clear(ctx, amt = 10):
    'To remove some lines from the history'
    await ctx.channel.purge(limit=amt+1)

@bot.command()
async def selfidentify(ctx, *, name):
    selfIdentify(ctx,name)
    await ctx.send(f'<@{ctx.author.id}> , you are identified as {name}')


@bot.command()
async def identify(ctx):
    m = ctx.message.mentions
    await findName(ctx.message,m[0])

# @bot.command()
# async def sdentify(ctx, *, name):
#     'To self identify a person'
#     await ctx.send(f'{ctx.author}, you are identified as {name}')
#
bot.run(open('token.txt', 'r').readline())