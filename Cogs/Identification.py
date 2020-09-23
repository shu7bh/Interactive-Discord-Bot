import discord
from discord.ext import commands
import os

class Identification(commands.Cog):
    
    def __init__(self,bot):
        self.bot=bot
    

    def removeName(self, userId):
        'To remove the identity of the user'
        isPresent = False
        with open("Resource/realNames.txt", 'r') as f:
            with open("Resource/temp.txt", 'w') as fout:
                for person in f:
                    if (str(userId)) == person.split(' = ', 1)[0]:
                        isPresent = True
                    else:
                        fout.write(person)
        if (isPresent):
            os.remove('Resource/realNames.txt')
            os.rename('Resource/temp.txt', 'Resource/realNames.txt')
            return "you are removed"
        
        return "your identity doesn't exist"


    def checkName(self,author):
        'Returns true if the name is already present in the list, else returns false'
        with open("Resource/realNames.txt", "r") as f:
            for person in f:
                if str(author.id) == tuple(person.split(" = ", 1))[0]:
                    return True
        return False

    def selfIdentify(self,_id, name):
        'Adds the name to the list'
        
        with open("Resource/realNames.txt","a+") as f:
            f.write(f'{_id} = {name}\n')


    def reidentify(self,_id,name):
        self.removeName(_id)
        self.selfIdentify(_id,name)

    def findName(self,person):
        'Gets the identified name of the mentioned user'

        with open("Resource/realNames.txt", "r+") as f:
            for entry in f:
                _id, name = entry.split(" = ", 1)
                if str(person.id) == _id:
                    return name
        return "not found\n"

    @commands.command(aliases = ['id'])
    async def identify(self,ctx):
        ' Aliases = id; You can find any users identity from here if they have added it'
        ans = ''
        for person in ctx.message.mentions:
            ans += f'{person} is {self.findName(person)}'
        await ctx.send(ans)


    @commands.command(aliases = ['selfid', 'sid'])
    async def selfidentify(self,ctx, *, name):
        'You can add your identity from here'
        author = ctx.author
        if self.checkName(author):
            self.reidentify(author.id, name)
            await ctx.send(f'{author} your identity has been updated to {name}')
            return
        
        self.selfIdentify(author.id ,name)
        await ctx.send(f'{author}, you are identified as {name}!')

    @commands.command(aliases = ['removeid', 'rid'])
    async def removeidentity(self,ctx):
        ' Aliases = removeid, rid; To remove your current identity'
        _id = ctx.author.id
        await ctx.send(f'{ctx.author} {self.removeName(_id)}')

def setup(bot):
    bot.add_cog(Identification(bot))