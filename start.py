# BOT: [PY] Discord bot base by VooDoo         #

# CODE A EDIT


__version__ = '1.1.0'
__author__ = 'VooDoo'

# Built-in Python Imports
import random
import os
import logging
import configparser

# Required for disocrd.py
import aiohttp
import discord
from discord.ext import commands

# DESCRIPTION
description = '''Discord Base Bot - Dev by VooDoo'''

# EXTENSION LOAD AT STARTUP
startup_extensions = [
    'modules.admin',
    'modules.autoreact',
    'modules.info',
    'modules.log',
    'modules.fortnitetest',
    'modules.fortnite',
    'modules.general',
    'modules.socialnetwork',
    'modules.poll',
    'modules.overwatch',
    'modules.random'
]

# Config for command and prefix
config = configparser.ConfigParser()
bot = commands.Bot(command_prefix='!')
config.read("config.ini")
TOKEN = config["TOKEN"]["token"] #Mettre votre token dans le fichier config.ini

prefix = '!' #Prefix des commandes


@bot.event
async def on_ready():
    bot.session = aiohttp.ClientSession(loop=bot.loop)
    bot.checkdev = lambda x: x == "012345678901234567" # Mettre votre identifiant Discord (le checkdev est pour voir si vous avez accès aux commandes du bot même) Où trouver l’ID de mon compte utilisateur/serveur/message ? https://support.discordapp.com/hc/fr/articles/206346498-Où-trouver-l-ID-de-mon-compte-utilisateur-serveur-message-
    bot.cogs['Log'].output('Connecté en tant que')
    bot.cogs['Log'].output("Nom d'utilisateur " + bot.user.name)
    bot.cogs['Log'].output("ID: " + bot.user.id)
    url = (
        "https://discordapp.com/api/oauth2/authorize?client_id=" +
        bot.user.id +
        "&scope=bot&permissions=8"
    )
    bot.cogs['Log'].output("Lien d'invitation du bot: " + url)

@bot.event
async def on_message(msg):
    if msg.content.startswith(prefix + "guess"):
        return
    if msg.author.bot:
        return
    await bot.process_commands(msg)

@bot.command()
async def load(extension_name : str):
    """Charge une extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Décharge une extension"""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
async def add(left : int, right : int):
    """Ajoute deux nombres ensemble."""
    await bot.say(left + right)

@bot.command()
async def repeat(times : int, content='répéter...'):
    """Répète un message plusieurs fois."""
    for i in range(times):
        await bot.say(content)

bot.remove_command('help')
@bot.command(pass_context=True, no_pm=False)
async def help(ctx):
    embed1 = discord.Embed(title="Général", description="Liste des commandes du bot:   Ne pas mettre les [] dans les commandes", color=0x279fe0)

    embed1.add_field(name="!PoF", value="Poop ou Face.", inline=False)
    embed1.add_field(name="!gn [Utilisateur]", value="Dire Bonne Nuit avec le bot.", inline=False)
    embed1.add_field(name="!pfc [pierre|feuille|ciseaux]", value="Pierre Feuille Ciseaux.", inline=False)
    embed1.add_field(name="!roll", value="Lance un dé et affiche le resultat.", inline=False)
    embed1.add_field(name="!ping", value="Pong !", inline=False)
    embed1.add_field(name="!bstats", value="Stats du bot.", inline=False)
    embed1.add_field(name='!poll ["question" "réponse 01" "réponse 02" "réponse 03" ...]', value="Faire un sondage.", inline=False)
    embed1.add_field(name='!face', value="Donne un face random. (+160 faces)", inline=False)
    embed1.add_field(name='!ball', value="Pose une question à BOT_NAME.", inline=False) # A EDIT
    embed1.add_field(name='!choose [option 1] [option 2]', value="BOT_NAME fait un choix.", inline=False) # A EDIT

    embed2 = discord.Embed(title="Social", description="Liste des commandes du bot:   Ne pas mettre les [] dans les commandes", color=0xe77bea)

    embed2.add_field(name="!discord", value="Donne le lien l'invitation du Discord de VOTRE DISCORD.", inline=False) # A EDIT
    embed2.add_field(name="!instagram", value="Donne le lien Instagram de NAME.", inline=False) # A EDIT
    embed2.add_field(name="!youtube", value="Donne le lien YouTube de NAME.", inline=False) # A EDIT
    embed2.add_field(name="!twitch", value="Donne le lien Twitch de NAME.", inline=False) # A EDIT
    embed2.add_field(name="!twitter", value="Donne le lien Twitter de NAME.", inline=False) # A EDIT
    embed2.add_field(name="!followers", value="Donne le nombre de followers de NAME.", inline=False) # A EDIT

    embed3 = discord.Embed(title="Overwatch", description="Liste des commandes du bot:   Ne pas mettre les [] dans les commandes", color=0xeee657)

    embed3.add_field(name="!owrng", value="Donne un perso random.", inline=False)
    embed3.add_field(name="!owteam", value="Donne une team random.", inline=False)
    embed3.add_field(name="!owstats <region (eu|us|asia)> <BattleTag (TonPseudo#12345)>", value="Donne les stats du joueur. (Ne fonctionne pas si toutes les stats ranked ne sont pas complètes.)", inline=False)

    embed4 = discord.Embed(title="Fortnite", description="Liste des commandes du bot:   Ne pas mettre les [] dans les commandes", color=0x8c35ec)

    embed4.add_field(name="!rdrop", value="Donne une ville random pour drop.", inline=False)
    embed4.add_field(name="!shop", value="Vous MP la boutique du jour.", inline=False)
    embed4.add_field(name="!stats <Platform (pc/psn/xbl)> <Pseudo EpicGames>", value="Donne les stats dans le channel #votre_channel_fortnite :warning: le pseudo doit être entre guillemets.", inline=False) # Mettre le nom de votre salon fortnite
    embed4.add_field(name="!wlist", value="Vous MP la liste des armes IG.", inline=False)
    embed4.add_field(name="!frstatus", value="Affiche si les serveurs Fortnite sont En ligne ou Hors ligne.", inline=False)

    embed5 = discord.Embed(title="Random", description="Uniquement pour les grades: VIP, Modo, Administrateur", color=0x0ec938) # Mettre vos grades

    embed5.add_field(name="!chat", value="Affiche une image/gif d'un chat random.", inline=False)
    embed5.add_field(name="!chien", value="Affiche une image/gif d'un chien random.", inline=False)

    await bot.delete_message(ctx.message)
    await bot.send_message(ctx.message.author, embed=embed1)
    await bot.send_message(ctx.message.author, embed=embed2)
    await bot.send_message(ctx.message.author, embed=embed3)
    await bot.send_message(ctx.message.author, embed=embed4)
    await bot.send_message(ctx.message.author, embed=embed5)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(TOKEN)
