import discord
from discord.ext import commands
import os

class Admin(commands.Cog):

    def __init__(self,bot):
        'To initialize the Admin Cog'
        
        self.bot = bot


    def cogPresent(self, extension):
        'To check if the file is present in the cog'

        return extension + '.py' in os.listdir('./Cogs')


    def _load(self, extension):
        'To load the Cog'
        
        if self.cogPresent(extension):
            self.bot.load_extension(f'Cogs.{extension}')
            return f'You have successfully added the {extension} cog'

        else:
            return 'No such Cog exists you noob! Being an admin lol'


    @commands.command(aliases = ['l'])
    async def load(self, ctx, extension):
        'To load Cogs'  

        await ctx.send(self._load(extension))

    
    def _unload(self, extension):
        'To unload the Cog'
        
        if self.cogPresent(extension):
            if (extension != 'Admin'):
                self.bot.unload_extension(f'Cogs.{extension}')
                return f'''You have successfully unloaded the {extension} cog.
            Be happy with the reduced functionality :(
            '''
            else:
                return 'You cannot unload the Admin cog'
        else:
            return 'No such Cog exists you noob! Being an admin lol'
        

    @commands.command(aliases = ['ul'])
    async def unload(self,ctx,extension):
        'To unload Cogs'

        await ctx.send(self._unload(extension))


    @commands.command(aliases = ['rl'])
    async def reload(self,ctx,extension):
        'To reload Cogs'
        
        if self.cogPresent(extension):
            self._unload(extension)
            self._load(extension)
            await ctx.send("You have successfully reloaded the Cog")
        else:
            await ctx.send("No such Cog exists you noob! Being an admin lol")


    @commands.command(aliases = ['remove'])
    async def clear(self,ctx, amt = 10):
        ' Aliases = remove; To remove some lines from the history'

        await ctx.channel.purge(limit=amt+1)


def setup(bot):
    bot.add_cog(Admin(bot))