from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import sys,os
import discord
import requests
from colorama import Fore, init
import pyfiglet
import time

os.system("title ๐ฟ๐๐จ๐ข๐ค๐ฃ๐ ๐๐ค๐ค๐ก ๐ฝ๐ฎ ๐๐๐ฅ๐๐๐ง")
os.system("cls")

def settings():
    print(Colorate.Horizontal(Colors.blue_to_purple, """
โโโ โ โโโโโ .โโโโยท  โ .โ            โ โขโ .โโ ยท 
โโยท โโโโโโ.โยทโโ โโโชโโโชโโโช     โช     โโโโโชโโ โ. 
โโโชโโโโโโโโโชโโโโโโโโโโโโ โโโโ  โโโโ โโโโยทโโโโโโ
โโโโโโโโโโโโโโโโโชโโโโโโโโโโ.โโโโโ.โโโโ.โโโโโโชโโ
 โโโโ โโช โโโ ยทโโโโ โโโ ยท โโโโโช โโโโโชยทโ  โ โโโโ
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