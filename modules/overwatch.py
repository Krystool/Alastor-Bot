# CODE A EDIT

import random
import requests
import asyncio
import json
import discord
from discord.ext import commands
import configparser
from utility import discordembed as dmbd
from random import choice as randchoice
from time import strftime


class Overwatch:

    def __init__(self, bot):
        self.bot = bot

        self.heroes = ['Genji', 'McCree', 'Pharrah', 'Faucheur', 'Soldat 76',
                       'Tracer', 'Bastion', 'Hanzo', 'Chacal', 'Mei',
                       'Torbjorn', 'Fatal', 'D.va', 'Reinhardt', 'Chopper',
                       'Winston','Zarya', 'Lucio', 'Ange', 'Symmetra', 
                       'Zenyatta', 'Sombra', 'Orisa', 'Doomfist', 'Ana', 'Brigitte', 'Moira']

        self.gif = ['https://i.pinimg.com/originals/05/57/fb/0557fbe4db1c69f754e7fa97ec940422.gif', 
                    'https://78.media.tumblr.com/9f09c9dfbcce86f4c18ba8c0b3ad9a5d/tumblr_p5dv03vM1B1swjm3io1_r1_500.gif', 
                    'https://78.media.tumblr.com/00ca780a54b11af0ebcdbfec69537659/tumblr_oep5ujqkaJ1vw9rjuo1_400.gif', 
                    'https://78.media.tumblr.com/0959fd64d3a4a9e17954c6d2980f97a4/tumblr_inline_ojn782LWM41rtrelo_500.gif', 
                    'https://78.media.tumblr.com/366aa76b9940428a444dccd319e169bc/tumblr_o85fm7upd11vw9rjuo1_400.gif', 
                    'https://orig00.deviantart.net/8ab5/f/2016/202/b/f/pixel_tracer_gif_by_crizard-daavt8w.gif', 
                    'https://pa1.narvii.com/6211/389600b8754d669e1993b9a6875a7024d0b6dc78_hq.gif'
                    ]

    @commands.command(pass_context=True)
    async def owrng(self, ctx):
        """ RNG OVERWATCH """
        msg = 'Joue '
        author = ctx.message.author
        em = dmbd.newembed(author, msg + randchoice(self.heroes))
        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=em)

    @commands.command(pass_context=True)
    async def owteam(self, ctx, num: int = 6):
        """ Obtenir une équipe OW Random \nUsage: owteam [Facultatif: Taille de l'équipe]"""
        random.shuffle(self.heroes)
        result = self.heroes[:num]
        msg = "Voici votre compo! Bonne chance! \n"
        results = "{}".format(", ".join(result))
        author = ctx.message.author
        em = dmbd.newembed(author, msg + results)
        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=em)

    @commands.command(aliases=["overwatchstats"], pass_context=True)
    async def owstats(self, ctx, region, username):
        """Overwatch Stats"""
        try:
            user = username.replace("#", "-")
            req = requests.get("https://ovrstat.com/stats/pc/" + region + "/" + user)
            # Mettre un nom sur les data
            st_json = json.loads(req.content.decode("utf-8"))
        except Exception as e:
            author = ctx.message.author
            title = 'Erreur API'
            c = 0xd30c0c
            desc = f'Code Erreur: {e}'
            em = dmbd.newembed(author, title, desc, c=0xd30c0c)
            self.stats_command = "```" + "!owstats <region (eu|us|kr)> <BattleTag (TonPseudo#12345)>" + "```"
            em.add_field(name='Utilisation de la commande:', value=self.stats_command)
            await self.bot.delete_message(ctx.message)
            await self.bot.say(embed=em)
        Ricon = st_json["ratingIcon"]
        icon = st_json["icon"]
        name = st_json["name"]
        level = st_json["level"]
        prestige = st_json["prestige"]
        Rlevel = st_json["rating"]
        gamesWon = st_json["gamesWon"]

        # QP Stats
        QP_eliminations = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["combat"]["eliminations"]
        QP_damageDone = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["combat"]["damageDone"]
        QP_deaths = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["combat"]["deaths"]
        QP_finalBlows = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["combat"]["finalBlows"]
        QP_environmentalKills = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["combat"]["environmentalKills"]
        QP_objectiveKills = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["combat"]["objectiveKills"]
        QP_timeSpentOnFire = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["combat"]["timeSpentOnFire"]
            # Victoire
        QP_timePlayed = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["game"]["timePlayed"]
        QP_gamesWon = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["game"]["gamesWon"]
            # Awards
        QP_cards = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["matchAwards"]["cards"]
        QP_medals = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["matchAwards"]["medals"]
        QP_medalsBronze = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["matchAwards"]["medalsBronze"]
        QP_medalsSilver = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["matchAwards"]["medalsSilver"]
        QP_medalsGold = st_json["quickPlayStats"]["careerStats"]["allHeroes"]["matchAwards"]["medalsGold"]

        # QP Stats
        RK_eliminations = st_json["competitiveStats"]["careerStats"]["allHeroes"]["combat"]["eliminations"]
        RK_damageDone = st_json["competitiveStats"]["careerStats"]["allHeroes"]["combat"]["damageDone"]
        RK_deaths = st_json["competitiveStats"]["careerStats"]["allHeroes"]["combat"]["deaths"]
        RK_finalBlows = st_json["competitiveStats"]["careerStats"]["allHeroes"]["combat"]["finalBlows"]
        RK_environmentalKills = st_json["competitiveStats"]["careerStats"]["allHeroes"]["combat"]["environmentalKills"]
        RK_objectiveKills = st_json["competitiveStats"]["careerStats"]["allHeroes"]["combat"]["objectiveKills"]
        RK_timeSpentOnFire = st_json["competitiveStats"]["careerStats"]["allHeroes"]["combat"]["timeSpentOnFire"]
            # Victoire
        RK_timePlayed = st_json["competitiveStats"]["careerStats"]["allHeroes"]["game"]["timePlayed"]
        RK_gamesWon = st_json["competitiveStats"]["careerStats"]["allHeroes"]["game"]["gamesWon"]
            # Awards
        RK_cards = st_json["competitiveStats"]["careerStats"]["allHeroes"]["matchAwards"]["cards"]
        RK_medals = st_json["competitiveStats"]["careerStats"]["allHeroes"]["matchAwards"]["medals"]
        RK_medalsBronze = st_json["competitiveStats"]["careerStats"]["allHeroes"]["matchAwards"]["medalsBronze"]
        RK_medalsSilver = st_json["competitiveStats"]["careerStats"]["allHeroes"]["matchAwards"]["medalsSilver"]
        RK_medalsGold = st_json["competitiveStats"]["careerStats"]["allHeroes"]["matchAwards"]["medalsGold"]


        # Mettre en forme le message
        st_embed = discord.Embed(
            title=f"Statistiques de {name}",
    		type="rich",
    		description=f"Region: {region} | Win: {gamesWon}",
    		colour=random.randint(0, 16777215)
        )
        st_embed.set_image(url=f"{randchoice(self.gif)}")
        st_embed.set_author(name=f"Afficher les stats de {name}",
    					icon_url="{0}".format(Ricon))
        st_embed.set_thumbnail(url=f"{icon}")
        st_embed.add_field(name="Level: ",
    						value=f"{level}\n\n")
        st_embed.add_field(name="Prestige: ",
    						value=f"{prestige}\n\n")
        st_embed.add_field(name="Level Ranked: ",
    						value=f"{Rlevel}\n\n")
        # QP
        st_embed.add_field(name="Statistiques",
                            value="QuickPlay / Ranked", inline=False)
        st_embed.add_field(name="Éliminations: ",
    						value=f"{QP_eliminations} / {RK_eliminations}")
        st_embed.add_field(name="Dégats Infligés: ",
    						value=f"{QP_damageDone} / {RK_damageDone}")
        st_embed.add_field(name="Morts: ",
    						value=f"{QP_deaths} / {RK_deaths}")
        st_embed.add_field(name="Coups de Grâce: ",
    						value=f"{QP_finalBlows} / {RK_finalBlows}")
        st_embed.add_field(name="Kills environnementale: ",
    						value=f"{QP_environmentalKills} / {RK_environmentalKills}")
        st_embed.add_field(name="Victimes sur Objectif: ",
    						value=f"{QP_objectiveKills} / {RK_objectiveKills}")
        st_embed.add_field(name="Temps on fire: ",
    						value=f"{QP_timeSpentOnFire} / {RK_timeSpentOnFire}")
        st_embed.add_field(name="Temps joué: ",
    						value=f"{QP_timePlayed} / {RK_timePlayed}")
        st_embed.add_field(name="Parties Gagnées: ",
    						value=f"{QP_gamesWon} / {RK_gamesWon}")
            # QP AWARD
        st_embed.add_field(name="Récompenses",
                            value="QuickPlay / Ranked", inline=False)
        st_embed.add_field(name="Cartes: ",
    						value=f"{QP_cards} / {RK_cards}")
        st_embed.add_field(name="Médailles: ",
    						value=f"{QP_medals} / {RK_medals}")
        st_embed.add_field(name="Bronze/Argent/Or: ",
    						value=f"QuickPlay: {QP_medalsBronze}/{QP_medalsSilver}/{QP_medalsGold} \n Ranked: {RK_medalsBronze}/{RK_medalsSilver}/{RK_medalsGold}")
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(self.bot.get_channel('1234567890'), ctx.message.author.mention, embed=st_embed) # Mettre l'ID du channel où les stats sont envoyés

def setup(bot):
    """ Setup OW Module"""
    bot.add_cog(Overwatch(bot))