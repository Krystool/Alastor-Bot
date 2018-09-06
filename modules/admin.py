
import asyncio
import time
import sys

import aiohttp
import discord
from discord.ext import commands
import logging
import utility.discordembed as dmbd

# Config for command and prefix
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
OWNER = config["GENERAL"]["owner"]
BOT_NAME = config["GENERAL"]["bot_name"]
ADMIN_RANK = config["GENERAL"]["admin"]
MODO_RANK = config["GENERAL"]["modo"]
VIP_PLUS_RANK = config["GENERAL"]["vip_plus"]
VIP_RANK = config["GENERAL"]["vip"]
NAME_SOCIAL = config["SOCIAL"]["social_name"]

class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, hidden=True)
    async def test(self, ctx, *, code: str):
        """ Teste quelque chose :o """
        if not self.bot.checkdev(ctx.message.author.id):
            return
        if code.startswith("```Python\n"):
            code = code[10:-3]
            start_time = time.time()
            try:
                exec(code)
                await self.bot.say("```Code exécuté```")
            except (TypeError, SyntaxError):
                await self.bot.say("```\n" + sys.exc_info() + "```")
                print("Erreur de syntaxe")
            total_time = time.time() - start_time
            await self.bot.say("Cela a pris *" + str(total_time) + "* secondes")

    @commands.command(pass_context=True, hidden=True)
    async def kys(self, ctx):
        """ Le Bot se tue """
        if not self.bot.checkdev(ctx.message.author.id):
            return
        await self.bot.say("*Mort du BOT dans 3 secondzs...*")
        await asyncio.sleep(3)
        await self.bot.close()

    @commands.command(pass_context=True, hidden=True)
    async def status(self, ctx, *, s: str):
        """ Change le Status """
        if not self.bot.checkdev(ctx.message.author.id):
            return
        await self.bot.change_presence(game=discord.Game(name=s))

    @commands.command(pass_context=True, hidden=True)
    async def changeavatar(self, ctx, *, url: str):
        """ Change L'Avatar"""
        if not self.bot.checkdev(ctx.message.author.id):
            return

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                if r.status == 200:
                    try:
                        await self.bot.edit_profile(avatar=await r.read())
                    except discord.HTTPException:
                        await self.bot.say("L'édition du profil a échoué.")
                    except discord.InvalidArgument:
                        await self.bot.say("Mauvais format d'image a été adopté.")

    @commands.command(pass_context=True, hidden=True)
    async def changeusername(self, ctx, *, s: str):
        """ Change le nom d'utilisateur """
        if self.bot.checkdev(ctx.message.author.id):
            await self.bot.edit_profile(username=s)

    @commands.command(pass_context=True, hidden=True)
    async def serverlist(self, ctx):
        if self.bot.checkdev(ctx.message.author.id):
            result = []
            for x in self.bot.servers:
                result.append(x.name)
            await self.bot.say("\n".join(result))

    @commands.command(pass_context=True, no_pm=False)
    @commands.has_role(ADMIN_RANK)
    async def ahelp(self, ctx):
        embed1 = discord.Embed(title="Général", description="Liste des commandes du bot:   Ne pas mettre les [] ou <> dans les commandes", color=0x279fe0)
    
        embed1.add_field(name="!PoF", value="Poop ou Face.", inline=False)
        embed1.add_field(name="!gn [Utilisateur]", value="Dire Bonne Nuit avec le bot.", inline=False)
        embed1.add_field(name="!pfc [pierre|feuille|ciseaux]", value="Pierre Feuille Ciseaux.", inline=False)
        embed1.add_field(name="!roll", value="Lance un dé et affiche le resultat.", inline=False)
        embed1.add_field(name="!ping", value="Pong !", inline=False)
        embed1.add_field(name="!bstats", value="Stats du bot.", inline=False)
        embed1.add_field(name='!poll ["question" "réponse 01" "réponse 02" "réponse 03" ...]', value="Faire un sondage.", inline=False)
        embed1.add_field(name='!face', value="Donne un face random. (+160 faces)", inline=False)
        embed1.add_field(name='!ball', value="Pose une question à "+BOT_NAME+".", inline=False)
        embed1.add_field(name='!choose [option 1] [option 2]', value=BOT_NAME+" fait un choix.", inline=False)
    
        embed2 = discord.Embed(title="Social", description="Liste des commandes du bot:   Ne pas mettre les [] ou <> dans les commandes", color=0xe77bea)
    
        embed2.add_field(name="!discord", value="Donne le lien l'invitation du Discord de "+NAME_SOCIAL+".", inline=False)
        embed2.add_field(name="!instagram", value="Donne le lien Instagram de "+NAME_SOCIAL+".", inline=False)
        embed2.add_field(name="!youtube", value="Donne le lien YouTube de "+NAME_SOCIAL+".", inline=False)
        embed2.add_field(name="!twitch", value="Donne le lien Twitch de "+NAME_SOCIAL+".", inline=False)
        embed2.add_field(name="!twitter", value="Donne le lien Twitter de "+NAME_SOCIAL+".", inline=False)
        embed2.add_field(name="!followers", value="Donne le nombre de followers "+NAME_SOCIAL+".", inline=False)
    
        embed3 = discord.Embed(title="Overwatch", description="Liste des commandes du bot:   Ne pas mettre les [] ou <> dans les commandes", color=0xeee657)
    
        embed3.add_field(name="!owrng", value="Donne un perso random.", inline=False)
        embed3.add_field(name="!owteam", value="Donne une team random.", inline=False)
        embed3.add_field(name="!owstats <region (eu|us|asia)> <BattleTag (TonPseudo#12345)>", value="Donne les stats du joueur. (Ne fonctionne pas si toutes les stats ranked ne sont pas complètes.)", inline=False)
    
        embed4 = discord.Embed(title="Fortnite", description="Liste des commandes du bot:   Ne pas mettre les [] ou <> dans les commandes", color=0x8c35ec)
    
        embed4.add_field(name="!rdrop", value="Donne une ville random pour drop.", inline=False)
        embed4.add_field(name="!shop", value="Vous MP la boutique du jour.", inline=False)
        embed4.add_field(name="!stats <Platform (pc/psn/xbl)> <Pseudo EpicGames>", value="Donne les stats dans le channel #fortnite :warning: le pseudo doit être entre guillemets.", inline=False)
        embed4.add_field(name="!wlist", value="Vous MP la liste des armes IG.", inline=False)
        embed4.add_field(name="!frstatus", value="Affiche si les serveurs Fortnite sont En ligne ou Hors ligne.", inline=False)
    
        embed5 = discord.Embed(title="Random", description="Uniquement pour les grades: "+VIP_PLUS_RANK+", "+MODO_RANK+", "+ADMIN_RANK, color=0x0ec938)
    
        embed5.add_field(name="!chat", value="Affiche une image/gif d'un chat random.", inline=False)
        embed5.add_field(name="!chien", value="Affiche une image/gif d'un chien random.", inline=False)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=embed1)
        await self.bot.say(embed=embed2)
        await self.bot.say(embed=embed3)
        await self.bot.say(embed=embed4)
        await self.bot.say(embed=embed5)

    @commands.command(pass_context=True, no_pm=False)
    @commands.has_role(ADMIN_RANK)
    async def modohelp(self, ctx):
        modo = discord.Embed(title="Commandes Modérations", description="Ne pas mettre les [] ou <> dans les commandes \n Commande uniquement pour les grades "+MODO_RANK+" et "+ADMIN_RANK+".", color=0x2de543)
    
        modo.add_field(name='!annonce "Votre texte d\'annonce" <code vidéo>', value="A faire dans le channel Annonces. \nLe bot va faire l'annonce automatiquement à votre place (avec un everyone + votre texte d\'annonce.)\nLe code de la vidéo toujours après watch?v= (Exemple: dans le lien `youtube.com/watch?v=eTRwF0iqIhg` le code est `eTRwF0iqIhg`')\nPour les liens mobile le code de la vidéo toujours après le dernier / (Exemple: dans le lien `https://youtu.be/czj39tAe2q0` le code est `czj39tAe2q0`')", inline=False)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=modo)

    @commands.command(pass_context=True, no_pm=False)
    @commands.has_role(ADMIN_RANK)
    async def generalhelp(self, ctx):
        general = discord.Embed(title="Général", description="Liste des commandes du bot:   Ne pas mettre les [] ou <> dans les commandes", color=0x279fe0)
    
        general.add_field(name="!PoF", value="Poop ou Face.", inline=False)
        general.add_field(name="!gn [Utilisateur]", value="Dire Bonne Nuit avec le bot.", inline=False)
        general.add_field(name="!pfc [pierre|feuille|ciseaux]", value="Pierre Feuille Ciseaux.", inline=False)
        general.add_field(name="!roll", value="Lance un dé et affiche le resultat.", inline=False)
        general.add_field(name="!ping", value="Pong !", inline=False)
        general.add_field(name="!bstats", value="Stats du bot.", inline=False)
        general.add_field(name='!poll ["question" "réponse 01" "réponse 02" "réponse 03" ...]', value="Faire un sondage.", inline=False)
        general.add_field(name='!face', value="Donne un face random. (+160 faces)", inline=False)
        general.add_field(name='!ball', value="Pose une question à "+BOT_NAME+".", inline=False)
        general.add_field(name='!choose [option 1] [option 2]', value=BOT_NAME+" fait un choix.", inline=False)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=general)

    @commands.command(pass_context=True, no_pm=False)
    @commands.has_role(ADMIN_RANK)
    async def socialhelp(self, ctx):
        social = discord.Embed(title="Social", description="Liste des commandes du bot:   Ne pas mettre les [] ou <> dans les commandes", color=0xe77bea)
    
        social.add_field(name="!discord", value="Donne le lien l'invitation du Discord de "+NAME_SOCIAL+".", inline=False)
        social.add_field(name="!instagram", value="Donne le lien Instagram de "+NAME_SOCIAL+".", inline=False)
        social.add_field(name="!youtube", value="Donne le lien YouTube de "+NAME_SOCIAL+".", inline=False)
        social.add_field(name="!twitch", value="Donne le lien Twitch de "+NAME_SOCIAL+".", inline=False)
        social.add_field(name="!twitter", value="Donne le lien Twitter de "+NAME_SOCIAL+".", inline=False)
        social.add_field(name="!followers", value="Donne le nombre de followers "+NAME_SOCIAL+".", inline=False)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=social)

    @commands.command(pass_context=True, no_pm=False)
    @commands.has_role(ADMIN_RANK)
    async def owhelp(self, ctx):
        ow = discord.Embed(title="Overwatch", description="Liste des commandes du bot:   Ne pas mettre les [] ou <> dans les commandes", color=0xeee657)
    
        ow.add_field(name="!owrng", value="Donne un perso random.", inline=False)
        ow.add_field(name="!owteam", value="Donne une team random.", inline=False)
        ow.add_field(name="!owstats <region (eu|us|asia)> <BattleTag (TonPseudo#12345)>", value="Donne les stats du joueur. (Ne fonctionne pas si toutes les stats ranked ne sont pas complètes.)", inline=False)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=ow)

    @commands.command(pass_context=True, no_pm=False)
    @commands.has_role(ADMIN_RANK)
    async def fortnitehelp(self, ctx):
        fortnite = discord.Embed(title="Fortnite", description="Liste des commandes du bot:   Ne pas mettre les [] ou <> dans les commandes", color=0x8c35ec)
    
        fortnite.add_field(name="!rdrop", value="Donne une ville random pour drop.", inline=False)
        fortnite.add_field(name="!shop", value="Vous MP la boutique du jour.", inline=False)
        fortnite.add_field(name="!stats <Platform (pc/psn/xbl)> <Pseudo EpicGames>", value="Donne les stats dans le channel #fortnite :warning: le pseudo doit être entre guillemets.", inline=False)
        fortnite.add_field(name="!wlist", value="Vous MP la liste des armes IG.", inline=False)
        fortnite.add_field(name="!frstatus", value="Affiche si les serveurs Fortnite sont En ligne ou Hors ligne.", inline=False)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=fortnite)

    @commands.command(pass_context=True, no_pm=False)
    @commands.has_role(ADMIN_RANK)
    async def randomhelp(self, ctx):
        random = discord.Embed(title="Random", description="Uniquement pour les grades:"+VIP_PLUS_RANK+", "+MODO_RANK+", "+ADMIN_RANK, color=0x0ec938)
    
        random.add_field(name="!chat", value="Affiche une image/gif d'un chat random.", inline=False)
        random.add_field(name="!chien", value="Affiche une image/gif d'un chien random.", inline=False)

        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=random)

def setup(bot):
    """Setup admin.py"""
    bot.add_cog(Admin(bot))
