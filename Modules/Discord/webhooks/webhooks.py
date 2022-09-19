from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import sys,os
import discord
import requests
from colorama import Fore, init
import pyfiglet
import time

os.system("title 𝘿𝙚𝙨𝙢𝙤𝙣𝙙 𝙏𝙤𝙤𝙡 𝘽𝙮 𝙕𝙖𝙥𝙝𝙞𝙧")
os.system("cls")

def settings():
    print(Colorate.Horizontal(Colors.blue_to_purple, """
▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·  ▄ .▄            ▄ •▄ .▄▄ · 
██· █▌▐█▀▄.▀·▐█ ▀█▪██▪▐█▪     ▪     █▌▄▌▪▐█ ▀. 
██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄██▀▐█ ▄█▀▄  ▄█▀▄ ▐▀▀▄·▄▀▀▀█▄
▐█▌██▐█▌▐█▄▄▌██▄▪▐███▌▐▀▐█▌.▐▌▐█▌.▐▌▐█.█▌▐█▄▪▐█
 ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀ ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪·▀  ▀ ▀▀▀▀
    	""", 1))

    print(Colorate.Horizontal(Colors.blue_to_purple, """
  1: Delete Webhooks                | 2:Spamm Webhooks 

  """, 1))
settings()
command = input(' choose -> ')

if command == '1':
    os.system('cmd /k "python Modules/Discord//webhooks///a.py"')


if command == '2':
    os.system('cmd /k "python Modules/Discord//webhooks///s.py"')