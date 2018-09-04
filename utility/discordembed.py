""" Discord Embed Default settings :D """
from time import strftime
import random

import discord

def newembed(a=None, t=None, d=None, u=None, c=None):
    if c is None:
        c = random.randint(0, 16777215)
    em = discord.Embed(title=t, description=d, url=u, colour=c)
    if a is not None:
        author = a.name + '#' + a.discriminator
        em.set_author(name=author, icon_url=a.avatar_url)
    em.set_footer(
        text="Propulsé par VooDoo | dear-voodoo.com",
        icon_url="http://dear-voodoo.com/coding/discord-bot/V-Animated.gif"
    )

    return em
