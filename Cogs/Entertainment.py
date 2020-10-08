import discord
from discord.ext import commands
import os
import random


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
        await context.send(f'Question: {q}\nAnswer: {random.choice(res)}')


def setup(bot):
    bot.add_cog(Entertainment(bot))