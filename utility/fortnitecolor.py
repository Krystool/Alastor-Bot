from time import strftime
import random

import discord
import json
import requests as req

def fortnitecolour():
    items_url = "https://fortnite-public-api.theapinetwork.com/prod09/store/get"
    items_headers = {'Authorization': '9f3b02bcaa8a878ef1cfe176ed8670b5'}
    items_data = req.post(
    	items_url, data={'language': 'en'}, headers=items_headers)
    items_json = json.loads(items_data.content.decode('utf-8'))
    items = items_json["items"]
    rarity_list = []
    for item in items:
    	rarity_list.append(item["item"]["rarity"])

    if rarity_list[0] == "uncommon":
        fc = 0x3c6f00
