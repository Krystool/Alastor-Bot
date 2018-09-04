# CODE A EDIT


# COLOR RARITY
# COMMON = 0x727272
# UNCOMMON = 0x3c6f00
# RARE = 0x22519c
# EPIC = 0x7525b9
# LEGENDARY = 0xf56b00
# MYTHIC = 0xd29600

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
import requests as req
import fnbr
import pynite

class Fortnite:
    """General commands."""

    def __init__(self, bot):
        self.bot = bot
        self.client = pynite.Client('VOTRE_API_KEY', timeout=5) # Mettre l'API_KEY Fortnite de ce site https://fortnitetracker.com/site-api (API KEY DES STATS)


# Random Drop
    @commands.command(pass_context=True)
    async def rdrop(self, ctx):
	    places = ["Risky Reels", "Lucky Landing", 
	    "China Motel", "New Factories", "Motel", "anywhere you want", 
	    "Football Ground", "Between Shifty and Flush", "Container", "Paradise Palms", 
	    "North of Wailing Woods","Dusty Divot","Fatal Fields", "Flush Factory", 
	    "Greasy Grove", "Haunted Hills", "Junk Junction", "Lonely Lodge", 
	    "Loot Lake","Pleasant Park", "Retail Row", "Salty Springs", "Lazy Links", 
	    "Shifty Shafts", "Snobby Shores", "Tilted Towers", "Tomato Town", "Wailing Woods"]
	    msg = 'Go '
	    author = ctx.message.author
	    em = dmbd.newembed(author, msg + randchoice(places))
	    await self.bot.delete_message(ctx.message)
	    await self.bot.say(embed=em)

# Shop
    @commands.command(pass_context=True)
    async def shop(self, ctx):
        apikey = 'VOTRE_API_KEY' # Mettre l'API_KEY Fortnite de ce site https://fnbr.co/api/docs (API KEY POUR LE SHOP)
        request = fnbr.Shop(apikey)
        response = request.send()
        if response.status == 200 and response.type == fnbr.constants.SHOP_TYPE:
            shop = response.data
            shp_embed = discord.Embed(
            	title="Liste des articles de la boutique en jeu (mise à jour quotidienne)",
            	type="rich",
            	colour=discord.Colour.gold()
            )
            shp_embed.set_author(name=f"Les articles de la boutique d'aujourd'hui sont: ",
                              icon_url="https://i.imgur.com/JijqpW9.jpg")
            await self.bot.delete_message(ctx.message)
            await self.bot.send_message(ctx.message.author, embed=shp_embed)
            for item in shop.daily:
                if item.rarity == "common":
                    self.rarity = 0x727272
                elif item.rarity == "uncommon":
                    self.rarity = 0x3c6f00
                elif item.rarity == "rare":
                    self.rarity = 0x22519c
                elif item.rarity == "epic":
                    self.rarity = 0x7525b9
                elif item.rarity == "legendary":
                    self.rarity = 0xf56b00
                elif item.rarity == "mythic":
                    self.rarity = 0xd29600
                shp_embed1 = discord.Embed(
        	    type="rich",
        	    colour=self.rarity
                )
                shp_embed1.set_author(name="{0}".format(item.name),
                                    icon_url="{0}".format(item.icon))
                shp_embed1.set_image(url="{0}".format(item.icon))
                shp_embed1.add_field(name="Nom de l'article:",
                                    value="{0}\n\n".format(item.name), inline=False)
                shp_embed1.add_field(name="Prix de l'article:",
                                    value="{0} VBUCKS\n\n".format(item.price), inline=False)
                shp_embed1.add_field(name="Rareté de l'article:",
                                    value="{0}\n\n".format(item.rarity), inline=False)
                shp_embed1.add_field(name="Type d'article:",
                                    value="{0}\n\n".format(item.type), inline=False)
                await self.bot.send_message(ctx.message.author, embed=shp_embed1)
            for item in shop.featured:
                if item.rarity == "common":
                    self.rarity = 0x727272
                elif item.rarity == "uncommon":
                    self.rarity = 0x3c6f00
                elif item.rarity == "rare":
                    self.rarity = 0x22519c
                elif item.rarity == "epic":
                    self.rarity = 0x7525b9
                elif item.rarity == "legendary":
                    self.rarity = 0xf56b00
                elif item.rarity == "mythic":
                    self.rarity = 0xd29600
                shp_embed0 = discord.Embed(
        	    type="rich",
        	    colour=self.rarity
                )
                shp_embed0.set_author(name="{0}".format(item.name),
                                    icon_url="{0}".format(item.icon))
                # item 1
                shp_embed0.set_image(url="{0}".format(item.icon))
                shp_embed0.add_field(name="Nom de l'article:",
                                    value="{0}\n\n".format(item.name), inline=False)
                shp_embed0.add_field(name="Prix de l'article:",
                                    value="{0} VBUCKS\n\n".format(item.price), inline=False)
                shp_embed0.add_field(name="Rareté de l'article:",
                                    value="{0}\n\n".format(item.rarity), inline=False)
                shp_embed0.add_field(name="Type d'article:",
                                    value="{0}\n\n".format(item.type), inline=False)
                await self.bot.send_message(ctx.message.author, embed=shp_embed0)
        else:
          await self.bot.say('Erreur d\'obtention de la boutique')

# Stats
    @commands.command(pass_context=True)
    async def stats(self, ctx, platform, username):
    	user = username.replace(" ", "%20")
    	player = await self.client.get_player(platform, user)
    	lifetime = await player.get_lifetime_stats()

        # Mettre en forme le message
    	st_embed = discord.Embed(
    	    title=f"Statistiques de {username}",
    		type="rich",
    		description=f"Nom en jeu: {username} | Platform: {platform}",
    		colour=random.randint(0, 16777215)
    	)
    	st_embed.set_author(name=f"Afficher les stats de {username}",
    					icon_url="")
    	st_embed.add_field(name="Statistiques",
    	                    value="Global", inline=False)
    	st_embed.add_field(name="TOP 1: ", value="{}".format(lifetime[8].value))
    	st_embed.add_field(name="TOP 10 (Solo): ", value="{}".format(lifetime[3].value))
    	st_embed.add_field(name="TOP 25 (Solo): ", value="{}".format(lifetime[5].value))
    	st_embed.add_field(name="Parties jouées: ", value="{}".format(lifetime[7].value))
    	st_embed.add_field(name="TOP 5 (Duo): ", value="{}".format(lifetime[0].value))
    	st_embed.add_field(name="TOP 12 (Duo): ", value="{}".format(lifetime[4].value))
    	st_embed.add_field(name="Pourcentage de Victoire: ", value="{}".format(lifetime[9].value))
    	st_embed.add_field(name="TOP 3 (Section): ", value="{}".format(lifetime[1].value))
    	st_embed.add_field(name="TOP 6 (Section): ", value="{}".format(lifetime[2].value))
    	st_embed.add_field(name="K/D: ", value="{}".format(lifetime[11].value))
    	st_embed.add_field(name="Kills: ", value="{}".format(lifetime[10].value))

    	await self.bot.delete_message(ctx.message)
    	await self.bot.send_message(self.bot.get_channel('1234567890'), ctx.message.author.mention, embed=st_embed) # Mettre l'ID du channel Fortnite

# Weapons List
    @commands.command(pass_context=True)
    async def wlist(self, ctx):
    	weaponList_url = "http://www.fortnitechests.info/api/weapons"
    	header_weaponList = {'accept': 'application/json'}
    	response_3 = req.get(weaponList_url, headers=header_weaponList)
    	weaponList_acquired = json.loads(response_3.content.decode("utf-8"))
    	# Get the list of all weapons by using the key 'name'
    	wList = [d['name'] for d in weaponList_acquired if 'name' in d]
    	# Using list(set()) get rid of duplicate entries in our list
    	wList = list(set(wList))
    	# Below code is written on purpose instead of using loops to prevent the bot from sending too many messages at once
    	wp1 = wList[0]
    	wp2 = wList[1]
    	wp3 = wList[2]
    	wp4 = wList[3]
    	wp5 = wList[4]
    	wp6 = wList[5]
    	wp7 = wList[6]
    	wp8 = wList[7]
    	wp9 = wList[8]
    	wp10 = wList[9]
    	wp11 = wList[10]
    	wp12 = wList[11]
    	wp13 = wList[12]
    	wp14 = wList[13]
    	wp15 = wList[14]
    	wp16 = wList[15]
    	wp17 = wList[16]
    	wp18 = wList[17]
    	wp19 = wList[18]
    	wp20 = wList[19]
    	wp21 = wList[20]
    	wp22 = wList[21]
    	wp23 = wList[22]
    	wp24 = wList[23]
    	wp25 = wList[24]

    	# Ready for output
    	wList = wp1 + "\n" + wp2 + "\n" + wp3 + "\n" + wp4 + "\n" + wp5 + "\n" + wp6 + "\n" + wp7 + "\n" + wp8 + "\n" + wp9 + "\n" + wp10 + "\n" + wp11 + \
                "\n" + wp12 + "\n" + wp13 + "\n" + wp14 + "\n" + wp15 + "\n" + wp16 + "\n" + wp17 + "\n" + wp18 + \
                "\n" + wp19 + "\n" + wp20 + "\n" + wp21 + "\n" + \
                wp22 + "\n" + wp23 + "\n" + wp24 + "\n" + wp25 + "\n"
    	wlist_embed = discord.Embed(
                        title="Obtenez la liste de toutes les armes disponibles dans le jeu",
                        type="rich",
                        description="Liste des Armes",
                        colour=random.randint(0, 16777215)
                    )
    	wlist_embed.set_author(name=f"Fortnite: Battle Royale",
                            icon_url="https://i.imgur.com/JijqpW9.jpg")
    	wlist_embed.add_field(name="Liste:",
                            value=f"{wList}\n\n", inline=False)
    	await self.bot.delete_message(ctx.message)
    	await self.bot.send_message(ctx.message.author, embed=wlist_embed)

# Status des serveurs
    @commands.command(pass_context=True)
    async def frstatus(self, ctx):
        st_url = "https://fortnite-public-api.theapinetwork.com/prod09/status/fortnite_server_status"
        st_headers = {'Authorization': 'VOTRE_ZPI_KEY'} # Mettre l'API_KEY Fortnite de ce site https://fortniteapi.com (API KEY POUR SAVOIR SI LES SERVEURS FORTNITE SONT EN LIGNE OU HORS LIGNE)
        st_data = req.post(st_url, headers=st_headers)
        st_json = json.loads(st_data.content.decode("utf-8"))
        UPorDOWN = st_json["status"]
        if UPorDOWN == "UP":
            STATUS = ":white_check_mark:  Les serveurs sont en ligne"
        else:
            STATUS = ":x: Les serveurs sont hors ligne"
        
        st_embed = discord.Embed(
            title=f"État des serveurs Fortnite",
        	type="rich",
        	description=f"{STATUS}",
        	colour=random.randint(0, 16777215)
        )
        await self.bot.delete_message(ctx.message)
        await self.bot.send_message(self.bot.get_channel('134567890'), ctx.message.author.mention, embed=st_embed) # Mettre l'ID du channel Fortnite

def setup(bot):
    """Setup Fortnite.py"""
    bot.add_cog(Fortnite(bot))