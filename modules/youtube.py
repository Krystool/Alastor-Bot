# CODE A EDIT

# Base import
import discord  # discord api
from discord.ext import commands  # commands extension
import configparser
import json
import requests
import urllib.request
from datetime import datetime
import time

# Module specific import
class Youtube:
    """General commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['a'])
    @commands.has_any_role("Modo", "Admin") # Mettre vos grades
    async def annonce(self, ctx, message, vidid):
        """Créer une annonce de vidéo/live youtube"""
        key = "API_KEY" # API KEY YOUTUBE
        channelid = "ID_DE_LA_CHAINE" # ID de la chaine youtube
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=snippet&id="+vidid+"&key="+key).read()
        titre = json.loads(data)["items"][0]["snippet"]["title"]
        miniature = json.loads(data)["items"][0]["snippet"]["thumbnails"]["maxres"]["url"]
        uploaddate = json.loads(data)['items'][0]['snippet']['publishedAt']
        realuploaddate = datetime.strptime(uploaddate, '%Y-%m-%dT%H:%M:%S.%fZ')
        uploader = json.loads(data)["items"][0]["snippet"]["channelTitle"]

        # Photo de profil
        data2 = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=snippet&id="+channelid+"&key="+key).read()
        PP = json.loads(data2)["items"][0]["snippet"]["thumbnails"]["high"]["url"]

        # Lien
        follow = "https://www.youtube.com/channel/"+channelid+"?sub_confirmation=1"
        sub = "https://gaming.youtube.com/USER/live?&action=sponsor" # Remplace USER par le nom de la chain Youtube Gaming

        YT = discord.Embed(title=f":tada: **{titre}**", colour=discord.Colour(value=0xf30000))
        YT.set_thumbnail(url=f"{PP}")
        YT.add_field(name=":link: Lien", value="https://youtube.com/watch?v={}".format(vidid), inline=False)
        YT.add_field(name=':heart:', value='[Abonne toi !]({})'.format(follow))
        YT.add_field(name=':green_heart:', value='[Devient sponsor !]({})'.format(sub))
        YT.set_image(url="{}".format(miniature))
        YT.set_footer(text='Upload le {0} par {1}'.format(realuploaddate, uploader), icon_url=f"{PP}")
        try:
            await self.bot.delete_message(ctx.message)
            await self.bot.say("@everyone \n{0}: {1}".format(ctx.message.author.display_name, message), embed=YT)
        except discord.HTTPException:
            await self.bot.say("On dirait que le bot n’a pas la permission pour les liens intégrés... Il en a besoin, alors je vous suggère de les ajouter!")

def setup(bot):
    n = Youtube(bot)
    bot.add_cog(n)