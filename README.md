# discord.py

[![Discord.py](https://img.shields.io/badge/Discord.py-0.16.6-green.svg)](https://pypi.python.org/pypi/discord.py/)

[![Python Version](https://img.shields.io/badge/Python-3.6.5%2B-blue.svg)](https://www.python.org)

discord.py is an API wrapper for Discord written in Python.

This was written to allow easier writing of bots or chat logs. Make sure to familiarise yourself with the API using the [documentation][doc].

**Légende:**
- [Information de base](https://github.com/dearvoodoo/discord-bot-base#inormation-de-base)
- [Installing](https://github.com/dearvoodoo/discord-bot-base#installing)
- [Requirements](https://github.com/dearvoodoo/discord-bot-base#requirements)
- [Configuration](https://github.com/dearvoodoo/discord-bot-base#configuration)
- [Commandes](https://github.com/dearvoodoo/discord-bot-base#commandes)

[doc]: http://discordpy.rtfd.org/en/latest
## INORMATION DE BASE
Je ne fais aucun support pour ce Bot. je fournis ici seulement mon code de base à vous à éditer comme bon vous semble. 
Une connaissance en Python avancé est extrêmement recommandée.

I do not support this Bot. I provide here only my basic code for you to edit as you see fit.
Advanced Python language knowledge is highly recommended.

## Installing

To install the library, you can just run the following command:

```
python3 -m pip install -U discord.py
```

## Requirements

- Python 3.6.5+
- All Requirements in requirements.txt

Versions:
![](https://img.shields.io/badge/aiohttp-1.0.5-orange.svg)
![](https://img.shields.io/badge/APScheduler-3.5.3-orange.svg)
![](https://img.shields.io/badge/astroid-1.6.3-orange.svg)
![](https://img.shields.io/badge/async-timeout-2.0.1-orange.svg)
![](https://img.shields.io/badge/asyncio-3.4.3-orange.svg)
![](https://img.shields.io/badge/attrs-18.1.0-orange.svg)
![](https://img.shields.io/badge/beautifulsoup4-4.6.0-orange.svg)
![](https://img.shields.io/badge/certifi-2018.4.16-orange.svg)
![](https://img.shields.io/badge/cffi-1.11.5-orange.svg)
![](https://img.shields.io/badge/chardet-3.0.4-orange.svg)
![](https://img.shields.io/badge/cleverwrap-0.2.3.6-orange.svg)
![](https://img.shields.io/badge/colorama-0.3.9-orange.svg)
![](https://img.shields.io/badge/colorlog-3.1.4-orange.svg)
![](https://img.shields.io/badge/config-0.4.0-orange.svg)
![](https://img.shields.io/badge/DateTime-4.2-orange.svg)
![](https://img.shields.io/badge/discord.py-0.16.12-orange.svg)
![](https://img.shields.io/badge/docopt-0.6.2-orange.svg)
![](https://img.shields.io/badge/feedparser-5.2.1-orange.svg)
![](https://img.shields.io/badge/fnbr-api-1.1.3-orange.svg)
![](https://img.shields.io/badge/future-0.16.0-orange.svg)
![](https://img.shields.io/badge/idna-2.6-orange.svg)
![](https://img.shields.io/badge/idna-ssl-1.0.1-orange.svg)
![](https://img.shields.io/badge/imgurpython-1.1.7-orange.svg)
![](https://img.shields.io/badge/isort-4.3.4-orange.svg)
![](https://img.shields.io/badge/keyboard-0.13.2-orange.svg)
![](https://img.shields.io/badge/lazy-object-proxy-1.3.1-orange.svg)
![](https://img.shields.io/badge/mccabe-0.6.1-orange.svg)
![](https://img.shields.io/badge/memory-profiler-0.54.0-orange.svg)
![](https://img.shields.io/badge/multidict-4.2.0-orange.svg)
![](https://img.shields.io/badge/oauthlib-2.1.0-orange.svg)
![](https://img.shields.io/badge/opuslib-3.0.1-orange.svg)
![](https://img.shields.io/badge/peewee-3.6.4-orange.svg)
![](https://img.shields.io/badge/Pillow-5.1.0-orange.svg)
![](https://img.shields.io/badge/pipreqs-0.4.9-orange.svg)
![](https://img.shields.io/badge/praw-6.0.0-orange.svg)
![](https://img.shields.io/badge/prawcore-1.0.0-orange.svg)
![](https://img.shields.io/badge/psutil-5.4.5-orange.svg)
![](https://img.shields.io/badge/pycountry-18.5.26-orange.svg)
![](https://img.shields.io/badge/pycparser-2.18-orange.svg)
![](https://img.shields.io/badge/pyfiglet-0.7.5-orange.svg)
![](https://img.shields.io/badge/pylint-1.8.4-orange.svg)
![](https://img.shields.io/badge/PyNaCl-1.0.1-orange.svg)
![](https://img.shields.io/badge/pynite-1.4.2-orange.svg)
![](https://img.shields.io/badge/python-box-3.2.0-orange.svg)
![](https://img.shields.io/badge/python-twitter-3.4.2-orange.svg)
![](https://img.shields.io/badge/pytz-2018.5-orange.svg)
![](https://img.shields.io/badge/requests-2.18.4-orange.svg)
![](https://img.shields.io/badge/requests-oauthlib-1.0.0-orange.svg)
![](https://img.shields.io/badge/six-1.11.0-orange.svg)
![](https://img.shields.io/badge/tabulate-0.8.2-orange.svg)
![](https://img.shields.io/badge/twitter-1.18.0-orange.svg)
![](https://img.shields.io/badge/tzlocal-1.5.1-orange.svg)
![](https://img.shields.io/badge/update-checker-0.16-orange.svg)
![](https://img.shields.io/badge/urbandictionary-1.1-orange.svg)
![](https://img.shields.io/badge/urllib3-1.22-orange.svg)
![](https://img.shields.io/badge/virtualenv-15.2.0-orange.svg)
![](https://img.shields.io/badge/virtualenv-clone-0.3.0-orange.svg)
![](https://img.shields.io/badge/websockets-3.4-orange.svg)
![](https://img.shields.io/badge/wikipedia-1.4.0-orange.svg)
![](https://img.shields.io/badge/wrapt-1.10.11-orange.svg)
![](https://img.shields.io/badge/xmltodict-0.11.0-orange.svg)
![](https://img.shields.io/badge/yarg-0.1.9-orange.svg)
![](https://img.shields.io/badge/yarl-1.2.3-orange.svg)
![](https://img.shields.io/badge/youtube-dl-2018.5.9-orange.svg)
![](https://img.shields.io/badge/zope.interface-4.5.0-orange.svg)



Usually `pip` will handle these for you.

## Configuration

Pour la configuration vous avez juste à edit le fichier `config.ini` il ressemble à ceci:
```ini
[GENERAL]
# Nom du BOT
bot_name = NAME

# ID du fondateur
owner = ID ICI

# ID de VooDoo
voodoo = 175006832002072576

# Nom du votre grade Administrateur
admin = ROLE ICI

#Nom de votre grade Modérateur
modo = ROLE ICI

#Nom de votre grade VIP+ (Si si il y en a pas)
vip_plus = ROLE ICI

#Nom de votre grade VIP (C'est un grade qui accès a plus de commande ex: !cat !dog)
vip = ROLE ICI

[TOKEN]
# Token du BOT Discord
token = TOKEN ICI

[YOUTUBE]
# Clé API Youtube DATA V3
api_key = API KEY ICI

# ID de la chaine Youtube
youtube_channel_id = API KEY ICI

# ex: https://gaming.youtube.com/USERNAME/live
youtube_gaming_url = URL ICI

[FORTNITE]
# Mettre l'API_KEY Fortnite de ce site https://fortnitetracker.com/site-api (API KEY DES STATS)
fortnitetracker = API KEY ICI

# Mettre l'API_KEY Fortnite de ce site https://fnbr.co/api/docs (API KEY POUR LE SHOP)
fnbr = API KEY ICI

# Mettre l'API_KEY Fortnite de ce site https://fortniteapi.com (API KEY POUR SAVOIR SI LES SERVEURS FORTNITE SONT EN LIGNE OU HORS LIGNE)
fortniteapi = API KEY ICI

# ID du channel Fortnite de votre Discord
fortnite_channel = ID CHANNEL ICI

[OVERWATCH]
# ID du channel Overwatch de votre Discord
overwatch_channel = ID CHANNEL ICI

[SOCIAL]
# Nom/Pseudo de la personne
social_name = NOM ICI

# Lien Twitter
twitter = URL ICI

# Lien Instagram
instagram = URL ICI

# Lien Youtube
youtube = URL ICI

# Lien Twitch
twitch = URL ICI

# Lien Discord
discord = URL ICI
```

## Commandes
### Général
Commande | Description
--- | --- 
!PoF | Poop ou Face.
!gn <Utilisateur> | Dire Bonne Nuit avec le bot.
!pfc <pierre/feuille/ciseaux> | Pierre Feuille Ciseaux.
!roll | Lance un dé et affiche le resultat.
!ping | Pong !
!bstats | Stats du bot.
!poll <"question" "réponse 01" "réponse 02" "réponse 03" ...> | Faire un sondage.
!face | Donne un face random. (+160 faces)
!ball | Pose une question à Squig.
!choose <option 1> <option 2> <...> | Squig fait un choix. Minimum 2 choix

### Social
Commande | Description
--- | --- 
!youtube | Donne le lien Youtube
!instagram | Donne le lien Instagram
!twitch | Donne le lien Twitch
!discord | Donne le lien Discord
!twitter | Donne le lien Twitter
!followers | Donne le nombre de followers

### Overwatch
Commande | Description
--- | --- 
!owrng | Donne un perso random.
!owteam | Donne une team random.
!owstats <region (eu/us/asia)> <BattleTag "TonPseudo#12345"> | Donne les stats du joueur. (Ne fonctionne pas si toutes les stats ranked ne sont pas complètes.) PC uniquement

### Fortnite
Commande | Description
--- | --- 
!rdrop | Donne une ville random pour drop.
!shop | Vous MP la boutique du jour.
!stats <pc/psn/xbl> "Pseudo EpicGames" | Donne les stats dans le channel #fortnite ⚠ le pseudo doit être entre guillemets.
!wlist | Vous MP la liste des armes IG.
!frstatus | Affiche si les serveurs Fortnite sont En ligne ou Hors ligne.

### Random
Commande | Description
--- | --- 
!cat | Affiche une image/gif d'un chat random.
!dog | Affiche une image/gif d'un chien random.
!reverse <texte> | La chose que vous m'avez dite, mais... à l'envers.

### Modération
Commande | Description
--- | --- 
!annonce "Votre texte d'annonce" <code vidéo> | Le bot va faire l'annonce automatiquement à votre place (avec un everyone + votre texte d'annonce.)
!annonce "Voici un test d'annonce via le bot" Ekrh04BeJ7U | ![alt text](https://image.ibb.co/gSwEFK/annonce_preview.png "Preview de la commande !annonce")
