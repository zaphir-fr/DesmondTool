from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import sys,os
import discord
import requests
from colorama import Fore, init
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")
os.system("cls")

def settings():
    print(Colorate.Horizontal(Colors.red_to_green, """

                        |||||||   
                       ( O   O ) 
                      oOO (_) OOo
    ████████▄   ▄█     ▄████████  ▄████████  ▄██████▄     ▄████████ ████████▄       
    ███   ▀███ ███    ███    ███ ███    ███ ███    ███   ███    ███ ███   ▀███ 
    ███    ███ ███▌   ███    █▀  ███    █▀  ███    ███   ███    ███ ███    ███ 
    ███    ███ ███▌   ███        ███        ███    ███  ▄███▄▄▄▄██▀ ███    ███                        
    ███    ███ ███▌ ▀███████████ ███        ███    ███ ▀▀███▀▀▀▀▀   ███    ███                         
    ███    ███ ███           ███ ███    █▄  ███    ███ ▀███████████ ███    ███                          
    ███   ▄███ ███     ▄█    ███ ███    ███ ███    ███   ███    ███ ███   ▄███                          
    ████████▀  █▀    ▄████████▀  ████████▀   ▀██████▀    ███    ███ ████████▀                           
                                                         ███    ███                                     
    	""", 1))                                                   

    print(Colorate.Horizontal(Colors.red_to_green, """
  1:  Backup Server                  | 2:  Nuke Server            | 17: Server Lookup
  3:  Checker Tokens                 | 4:  Logs Server Token      | 18: Crash Owner Token
  5:  DM All Friends                 | 6:  Manage Webhooks
  7:  Mass ask friends (tokens)      | 8:  Join Server (beta)
  9:  Fake Ping (id)                 | 10: Change The Statuses
  11: All Tokens Online              | 12: Delete All Friends
  13: Leave All Server               | 14: Close All Dm
  15: Token Lookup                   | 16: User id Lookup

    	""", 1))
settings()

command = input(Colorate.Horizontal(Colors.red_to_green, '\n[>] choose -> '))

if command == '1':
   os.system('cmd /k "python Modules//Discord///Backup////a.py"')

if command == '2':
   os.system('cmd /k "python Modules//Discord///NukeServer////b.py"')

if command == '3':
   os.system('cmd /k "python Modules//Discord///Check////checker.py"')

if command == '4':
   os.system('cmd /k "python Modules//Discord///Nukeacc////Nuker.py"')

if command == '5':
    os.system('cmd /k "python Modules//Discord///dmall////dmall.py"')

if command == '6':
    os.system('cmd /k "python Modules//Discord///webhooks////webhooks.py"')

if command == '7':
    os.system('cmd /k "python Modules//Discord///friend////friend.py"')

if command == '8':
    os.system('cmd /k "python Modules//Discord///join////join.py"')

if command == '9':
    os.system('cmd /k "python Modules//Discord///ping////ping.py"')

if command == '10':
    os.system('cmd /k "python Modules//Discord///sta////ChangeStatus.py"')

if command == '11':
    os.system('cmd /k "python Modules//Discord///x////main.py"')

if command == '11':
    os.system('cmd /k "python Modules//Discord///xw////xw.py"')

if command == '12':
    os.system('cmd /k "python Modules//Discord///f////f.py"')

if command == '13':
    os.system('cmd /k "python Modules//Discord///fff////ff.py"')

if command == '14':
    os.system('cmd /k "python Modules//Discord///za////za.py"')

if command == '15':
    os.system('cmd /k "python Modules//Discord///zs////zs.py"')

if command == '16':
    os.system('cmd /k "python Modules//Discord///id////id.py"')

if command == '17':
    os.system('cmd /k "python Modules//Discord///sl////sl.py"')

if command == '18':
    os.system('cmd /k "python Modules//Discord///spam////spam.py"')