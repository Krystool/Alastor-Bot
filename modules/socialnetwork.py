# CODE A EDIT

from datetime import datetime
import time
import urllib.request
import json

from discord.ext import commands
import psutil
import utility.discordembed as dmbd

class Social:
    """Liens des reseaux sociaux!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def twitter(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà le Twitter de USERNAME\n' + # A EDIT
            'https://twitter.com/USERNAME' # A EDIT
        )
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def instagram(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà l\'Instagram de USERNAME\n' + # A EDIT
            'https://www.instagram.com/USERNAME/' # A EDIT
        )
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def youtube(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà le YouTube de USERNAME\n' + # A EDIT
            'https://www.youtube.com/USERNAME' # A EDIT
        )
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def twitch(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà le Twitch de USERNAME\n' + # A EDIT
            'https://www.twitch.tv/USERNAME' # A EDIT
        )
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def discord(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà le lien d\'invitation du Discord de VOTRE_DISCORD\n' + # A EDIT
            'https://discordapp.com/invite/CODE' # A EDIT
        )
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def followers(self, ctx):
        key = "VOTRE_API_KEY"  # Mettre votre API_KEY Youtube V3 https://developers.google.com/youtube/v3/getting-started
        chaine = "ID DE LA CHAINE" # Mettre l'ID de la chaine youtube 
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+chaine+"&key="+key).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        description = (
            "USERNAME à " + "{:,d}".format(int(subs)) + " subscribers!🎉" # A EDIT
        )
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(embed=em)


def setup(bot):
    n = Social(bot)
    bot.add_cog(n)