import discord
import os
import time
import requests
import random
import string
import colorama
from colorama import Fore
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")
Token = input('   path to .txt ->')
UserID = input("Enter user ID: ")
with open((Token), 'r') as Tokens:
    friends = 0
    tkens = []
    for line in Tokens:
        tkens.append(line.strip())
    for Token in tkens:
        headers = {
            "Authorization": f"{Token}"
        }
        payload = {'' : ''}
        r = requests.put(f"https://discordapp.com/api/v8/users/@me/relationships/{UserID}", headers=headers, json=payload)
        if r.status_code == 200:
            friends += 1
            print(f"{Fore.GREEN}[Status]: {Fore.RESET} Succesfully sent friend request")
        elif f"{Fore.RED}[Error]: {Fore.RESET} Couldnt send a friend request" in r.text:
            print(f"{Fore.RED}Error.")
        else:
            print(f"{Fore.RED}[Error]: {Fore.RESET} Invalid ID")
        time.sleep(2)


os.system("pause")

os.system('cmd /k "python DesmondTool.py"')