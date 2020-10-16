import discord
from discord.ext import commands
import youtube_dl
import asyncio

players = {}

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)



class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=["j"])
    async def join(self, ctx):
        'This will join the voice channel in which the user is in'

        await ctx.author.voice.channel.connect()

    @commands.command(aliases=["l"])
    async def leave(self, ctx):
        'This will leave the voice channel in the server'

        await ctx.voice_client.disconnect()

    @commands.command(aliases=["p"])
    async def play(self, ctx, url):
        'The play command will play the youtube url in the message'

        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            voice_channel.play(player, after=lambda e: print ('Player error: %s' %e) if e else None)

        await ctx.send(f"**Now Playing: ** {player.title}")


    @join.error
    async def join_error(self, ctx, error):
        print(error)

    @play.error
    async def play_error(self, ctx, error):
        print(error)

def setup(bot):
    bot.add_cog(Music(bot))