from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import colorama
from colored import fg, attr
from colorama import Fore, Back, Style, init
import requests
from time import sleep
import os
import os.path
from requests.api import options
import sys
import webbrowser
os.system('cls' if os.name == 'nt' else 'clear')
colorama.init(autoreset=True)
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")


headers = {
'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
'Authorization' : input(Colorate.Horizontal(Colors.red_to_green, f"\nEnter Your Token. [>] "))
}


guildId = input(Colorate.Horizontal(Colors.red_to_green, f"\n Enter Guild ID. [>] "))

response = requests.get(
    f"https://discord.com/api/guilds/{guildId}",
    headers = headers ,
    params = {"with_counts" : True}
    ).json()


owner = requests.get(
    f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
    headers = headers,
    params = {"with_counts" : True}
    ).json()

print(Colorate.Horizontal(Colors.red_to_green, f"""
    Guild/Server | Name > {response['name']} 
    Guild/Server | ID > {response['id']}
    Guild/Server | Icon URL > https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
    Guild/Server | Approxomate Amount of Members > {response['approximate_member_count']}
    Guild/Server | Owner > {owner['user']['username']}#{owner['user']['discriminator']} 
    Guild/Server | Owner ID > {response['owner_id']}
    Guild/Server | Region > {response['region']}
    """))

os.system("pause")

os.system('cmd /k "python DesmondTool.py"')

