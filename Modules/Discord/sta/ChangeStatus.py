import discord
import json
import requests
import ctypes
import os
import time

Token = input('token ->')
status1 = input('Status 1 ->')
status2 = input('Status 2 ->')
status3 = input('Status 3 ->')

headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
for i in range(0, 50):
    json = {"custom_status": {"text": (status1), "emoji_name": "🛸"}}
    requests.patch(
        "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
    )
    time.sleep(0.7)
    json = {"custom_status": {"text": (status2), "emoji_name": "🚀"}}
    requests.patch(
        "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
    )
    time.sleep(0.7)
    json = {"custom_status": {"text": (status3), "emoji_name": "💊"}}
    requests.patch(
        "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
    )
    time.sleep(0.7)