import discord
from discord.ext import commands
from discord.utils import get
import os

aliases = {
    'A': 'Admin',
    'admin': 'Admin',
    'E': 'Entertainment',
    'entertainment': 'Entertainiment',
    'I': 'Identification',
    'identification': 'Identification'
}

class Admin(commands.Cog):

    def __init__(self,bot):
        'To initialize the Admin Cog'
        
        self.bot = bot


    def cogPresent(self, extension):
        'To check if the file is present in the cog'

        return extension + '.py' in os.listdir('./Cogs')


    def _load(self, extension):
        'To load the Cog'

        if extension in aliases.keys():
            extension = aliases[extension]
        
        if self.cogPresent(extension):
            try:
                self.bot.load_extension(f'Cogs.{extension}')
                return f'You have successfully added the {extension} cog'
            except:
                return f'The {extension} Cog is already loaded'

        else:
            return 'No such Cog exists you noob! Being an admin lol'

    async def cog_check(self, ctx):
        'Check if user has admin role'

        #admin = get(ctx.guild.roles, name="Admin")
        #return admin in ctx.author.roles

        return ctx.author.guild_permissions.manage_messages \
            or ctx.author.guild_permissions.manage_guild \
            or ctx.author.guild_permissions.manage_channels \
            or ctx.author.guild_permissions.administrator

    @commands.command(aliases = ['l'])
    async def load(self, ctx, extension):
        'To load Cogs'  

        await ctx.send(self._load(extension))

    
    def _unload(self, extension):
        'To unload the Cog'

        if extension in aliases.keys():
            extension = aliases[extension]
        
        if self.cogPresent(extension):
            if (extension != 'Admin'):
                try:
                    self.bot.unload_extension(f'Cogs.{extension}')
                    return f'''You have successfully unloaded the {extension} cog.
                    Be happy with the reduced functionality :(
                    '''
                except:
                    return f'The {extension} Cog is already unloaded'
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

        if extension in aliases.keys():
            extension = aliases[extension]
        
        if self.cogPresent(extension):
            self._unload(extension)
            self._load(extension)
            await ctx.send("You have successfully reloaded the Cog")
        else:
            await ctx.send("No such Cog exists you noob! Being an admin lol")


    @commands.command(aliases = ['remove'])
    async def clear(self,ctx, amt):
        'Aliases = remove; To remove some lines from the history'

        await ctx.channel.purge(limit=amt+1)

    @unload.error
    async def unload_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Give the correct Cog name')

    @load.error
    async def load_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Give the correct extension')

    @reload.error
    async def reload_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Give the desired extension')
            
    @clear.error
    @commands.has_guild_permissions(manage_messages = True)
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await('Give an integer value to delete')

    @clear.error
    @commands.has_guild_permissions(manage_messages = False)
    async def _clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await('Give an integer value to delete')
        else:
            await('The bot does not have manage message permission')

def setup(bot):
    bot.add_cog(Admin(bot))