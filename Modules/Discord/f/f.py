import requests
import discord
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")

Token = input(' Token ->')
headers = {"authorization": Token, "user-agent": "bruh6/9"}
remove_friends_request = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
for i in remove_friends_request:
    requests.delete(
        f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
        headers=headers,
        )
    print(f"Removed Friend {i['id']}")


os.system("pause")

os.system('cmd /k "python DesmondTool.py"')