import discord
from discord.ext import commands
import random
import os

bot = commands.Bot(command_prefix = '!')

def checkName(author):
    'Returns true if the name is already present in the list, else returns false'

    with open("realNames.txt", "r") as f:
        for person in f:
            if str(author.id) == tuple(person.split(" = ", 1))[0]:
                return True
    return False


def selfIdentify(_id, name):
    'Adds the name to the list'

    with open("realNames.txt","a+") as f:
        f.write(f'{_id} = {name}\n')


def findName(person):
    'Gets the identified name of the mentioned user'

    with open("realNames.txt", "r+") as f:
        for entry in f:
            _id, name = entry.split(" = ", 1)
            if str(person.id) == _id:
                return name
    return "not found\n"


def removeName(userId):
    'To remove the identity of the user'

    isPresent = False
    with open("realNames.txt", 'r') as f:
        with open("temp.txt", 'w') as fout:
            for person in f:
                if (str(userId)) == person.split(' = ', 1)[0]:
                    isPresent = True
                else:
                    fout.write(person)
    if (isPresent):
        os.remove('realNames.txt')
        os.rename('temp.txt', 'realNames.txt')
        return "you are removed"
    
    return "your identity doesn't exist"


def reidentify(_id,name):
    removeName(_id)
    selfIdentify(_id,name)

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
    ' Aliases = 8ball; A fun section where the bot predicts answers'

    res = list(open('8ballResponses.txt', 'r').readlines())
    await context.send(f'Question: {q}\nAnswer: {random.choice(res)}')


@bot.command(aliases = ['remove'])
async def clear(ctx, amt = 10):
    ' Aliases = remove; To remove some lines from the history'

    await ctx.channel.purge(limit=amt+1)


@bot.command(aliases = ['selfid', 'sid'])
async def selfidentify(ctx, *, name):
    'You can add your identity from here'

    author = ctx.author
    if checkName(author):
        reidentify(author.id, name)
        await ctx.send(f'{author} your identity has been updated to {name}')
        return
    
    selfIdentify(author.id ,name)
    await ctx.send(f'{author}, you are identified as {name}!')


@bot.command(aliases = ['id'])
async def identify(ctx):
    ' Aliases = id; You can find any users identity from here if they have added it'

    ans = ''
    for person in ctx.message.mentions:
        ans += f'{person} is {findName(person)}'
    await ctx.send(ans)


@bot.command(aliases = ['removeid', 'rid'])
async def removeidentity(ctx):
    ' Aliases = removeid, rid; To remove your current identity'

    _id = ctx.author.id
    await ctx.send(f'{ctx.author} {removeName(_id)}')

bot.run(open('token.txt', 'r').readline())