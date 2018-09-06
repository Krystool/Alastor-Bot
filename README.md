# discord.py

[![PyPI](https://img.shields.io/pypi/v/discord.py.svg)](https://pypi.python.org/pypi/discord.py/)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://pypi.python.org/pypi/discord.py/)

discord.py is an API wrapper for Discord written in Python.

This was written to allow easier writing of bots or chat logs. Make sure to familiarise yourself with the API using the [documentation][doc].

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

- Python 3.4.2+
- All Requirements in requirements.txt

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
