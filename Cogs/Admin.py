import discord
from discord.ext import commands
from discord.utils import get
from Resource.aliases import aliases
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
    @commands.bot_has_permissions(manage_messages = True)
    async def clear(self,ctx, amt):
        'Aliases = remove; To remove some lines from the history'

        if amt.isdigit():
            await ctx.channel.purge(limit=int(amt)+1)
        else:
            await ctx.send('Enter a number')
            

    @commands.command(aliases=['b'])
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self,ctx):
        'Ban a member from the server'
        await ctx.send(f'atleast it is coming here')
        for person in ctx.message.mentions:
            await ctx.guild.ban(person)
            await ctx.send(f'<@{person.id}> has been banned')


    @commands.command(aliases=['ub'])
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
        'Unban a member from the server'

        member = member.split(' ')
        member = [mem.split('#') for mem in member]
        
        for mem_name, mem_dis in member:
            for user in [banned_entry.user for banned_entry in await ctx.guild.bans()]:
                if(user.name, user.discriminator) == (mem_name, mem_dis):
                    await ctx.guild.unban(user)
                    await ctx.send(f'<@{user.id}> has been unbanned')
                    break
        
                    
    @commands.command(aliases=['k'])
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self,ctx):
        'Kick a member from the server'
        
        for person in ctx.message.mentions:
            await ctx.guild.kick(person)
            await ctx.send(f'<@{person.id}> has been kicked from the server')
    
    
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
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify the number of messages you want to clear')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"The Bot needs: {' '.join(error.missing_perms)}")


    @ban.error
    async def ban_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send('Please mention the user you want to ban')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"The Bot needs: {' '.join(error.missing_perms)}")


    @unban.error
    async def unban_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send('Please mention the user you want to unban')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"The Bot needs: {' '.join(error.missing_perms)}")


    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send('Please mention the user you want to kick')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"The Bot needs: {' '.join(error.missing_perms)}")
            
def setup(bot):
    bot.add_cog(Admin(bot))