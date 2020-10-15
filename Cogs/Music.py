import discord
from discord.ext import commands
import youtube_dl


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['j'])
    async def join(self, ctx):
        # channel = ctx.author.voice.channel
        await ctx.author.voice.channel.connect()

    @commands.command(aliases=['l'])
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @join.error
    async def join_error(self, ctx, error):
        print(error)


def setup(bot):
    bot.add_cog(Music(bot))