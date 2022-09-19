import discord
import json
import requests
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")

Token = input('Token ->')
headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
leave_all_servers_request = requests.get(
    "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
    ).json()
for guild in leave_all_servers_request:
    requests.delete(
        f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
        headers=headers,
        )
    print(f"Left Guild: {guild['id']}")

os.system("pause")

os.system('cmd /k "python DesmondTool.py"')