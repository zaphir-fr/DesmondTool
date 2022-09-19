import requests
import random
import string
from time import sleep
from colorama import Fore
import os
import ctypes 



ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")

Token = input('token ->')



def headers(Token):
    leaders = {"authorization": Token}
    return leaders





headers(Token)


print("-"*20)
r = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers(Token))
jsson = r.json()
for i in jsson:
    print(i)
    print("-"*20)
print('permissions': '4398046511103 Admin   ')


os.system("pause")

os.system('cmd /k "python DesmondTool.py"')