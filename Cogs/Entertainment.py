import discord
from discord.ext import commands
import os
from random import choice, randint
import requests

class Entertainment(commands.Cog):
    """The Entertainment section is where you can pass your time fruitlessly with
        the various options available to you!!
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, context):
        'To get the time taken by the bot to reply'

        await context.send(f'{round(self.bot.latency * 1000)}ms')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, context, *, q):
        ' Aliases = 8ball; A fun section where the bot predicts answers'

        res = list(open('Resource/8ballResponses.txt', 'r').readlines())
        await context.send(f'Question: {q}\nAnswer: {choice(res)}')

    @commands.command(aliases=['telljoke'])
    async def joke(self,ctx):
        ' Tells a random joke '
        responses = requests.get("https://official-joke-api.appspot.com/random_joke").json()

        jokeSetup = responses['setup']
        jokePunchline = responses['punchline']
        await ctx.send(f'{jokeSetup}\n{jokePunchline}')
        
    @commands.command(aliases=['rand'])
    async def random(self, ctx, a, b):
        ' Generates a random number between the two given numbers '
        
        await ctx.send(f'You have picked: {randint(int(a), int(b))}')

    @commands.command()
    async def roll(self,ctx):
        ' Rolls a die and give a random number between 1 and 6 '
        await ctx.send(f'You have rolled the die...')
        await ctx.send(f'You rolled a {randint(1,6)}!')
        
def setup(bot):
    bot.add_cog(Entertainment(bot))
