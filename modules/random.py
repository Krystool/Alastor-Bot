# For check role @commands.has_role("name")

# Base import
import discord
from discord.ext import commands
import utility.discordembed as dmbd
import configparser
import json


# Module specific import
import random
from random import choice
from random import choice as randchoice
import requests
from bs4 import BeautifulSoup

# Config
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
ADMIN_RANK = config["GENERAL"]["admin"]
MODO_RANK = config["GENERAL"]["modo"]
VIP_PLUS_RANK = config["GENERAL"]["vip_plus"]
VIP_RANK = config["GENERAL"]["vip"]

class Random:
    """Random commands."""

    def __init__(self, bot):
        self.bot = bot

# Say random cat images
    @commands.command(pass_context=True, aliases=['chat', 'minou'])
    @commands.has_any_role(ADMIN_RANK, MODO_RANK, VIP_PLUS_RANK, VIP_RANK)
    async def cat(self, ctx):
        """ Lorsque les utilisateurs tapent !cat, renvoyer un lien de chat """
        req = requests.get('http://thecatapi.com/api/images/get.php')
        if req.status_code != 200:
            print("Impossible d'obtenir un chat")
        rngcat = req.url
        author = ctx.message.author
        title = 'TheCatAPI.com'
        desc = 'Voilà, un chat.'
        url = rngcat
        em = dmbd.newembed(author, title, desc, url)
        em.set_image(url=rngcat)
        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=em)

# Say random dog images
    @commands.command(pass_context=True, aliases=['chien', 'toutou'])
    @commands.has_any_role(VIP_RANK, VIP_PLUS_RANK, MODO_RANK, ADMIN_RANK)
    async def dog(self, ctx):
        """Lorsque les utilisateurs tapent !dog, renvoyer un lien de chien"""

        req = requests.get('http://random.dog/')
        if req.status_code != 200:
            print("Impossible d'obtenir un chien")
        doglink = BeautifulSoup(req.text, 'html.parser')
        rngdog = 'http://random.dog/' + doglink.img['src']
        author = ctx.message.author
        title = 'Random.Dog'
        desc = 'Voilà, un chien.'
        url = rngdog
        em = dmbd.newembed(author, title, desc, url)
        em.set_image(url=rngdog)
        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=em)

# Reverse le texte
    @commands.command(pass_context=True)
    async def reverse(self, ctx, *, Message:str):
        """La chose que vous m'avez dite, mais .. à l'envers."""
        await self.bot.say(u"\u200B" + Message[::-1])




def setup(bot):
    """Setup Random.py"""
    bot.add_cog(Random(bot))