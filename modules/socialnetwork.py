from datetime import datetime
import time
import urllib.request
import json

from discord.ext import commands
import psutil
import utility.discordembed as dmbd

import configparser
config = configparser.ConfigParser()
config.read("config.ini")
NAME_SOCIAL = config["SOCIAL"]["social_name"]
URL_TWITTER = config["SOCIAL"]["twitter"]
URL_INSTAGRAM = config["SOCIAL"]["instagram"]
URL_YOUTUBE = config["SOCIAL"]["youtube"]
URL_TWITCH = config["SOCIAL"]["twitch"]
URL_DISCORD = config["SOCIAL"]["discord"]
API_KEY = config["YOUTUBE"]["api_key"]
CHANNEL_ID = config["YOUTUBE"]["youtube_channel_id"]

class Social:
    """Liens des reseaux sociaux!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def twitter(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà le Twitter de '+NAME_SOCIAL+'\n' + URL_TWITTER)
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def instagram(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà l\'Instagram de '+NAME_SOCIAL+'\n' + URL_INSTAGRAM)
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def youtube(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà le YouTube de '+NAME_SOCIAL+'\n' + URL_YOUTUBE)
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def twitch(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà le Twitch de '+NAME_SOCIAL+'\n' + URL_TWITCH)
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def discord(self, ctx):
        second = ctx.message.author.mention
        description = (
            'Voilà le lien d\'invitation du Discord de '+NAME_SOCIAL+'\n' + URL_DISCORD)
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(second, embed=em)

    @commands.command(pass_context=True)
    async def followers(self, ctx):
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+CHANNEL_ID+"&key="+API_KEY).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        description = (
            NAME_SOCIAL + " à " + "{:,d}".format(int(subs)) + " followers!🎉"
        )
        em = dmbd.newembed(ctx.message.author, d=description)
        await self.bot.say(embed=em)


def setup(bot):
    n = Social(bot)
    bot.add_cog(n)