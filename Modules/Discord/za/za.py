import discord
import requests
import json

Token = input('tokens ->')
headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
close_dm_request = requests.get(
	"https://canary.discord.com/api/v8/users/@me/channels", headers=headers
	).json()
for channel in close_dm_request:
	requests.delete(
		f"https://canary.discord.com/api/v8/channels/{channel['id']}",
		headers=headers,
		)