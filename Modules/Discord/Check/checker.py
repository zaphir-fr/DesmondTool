from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, Back, Style
import requests
import json
import os
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")

ids = []
checked = []

invalid = []
working = []
verified = []
phone = []
billing = []
nitro = []

try: 
    os.mkdir('resultsTokens')
except OSError as error: 
    print(error) 

os.system("cls")

print(Colorate.Horizontal(Colors.red_to_green, """
 ▄████████    ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄    ▄████████    ▄████████ 
███    ███   ███    ███     ███    ███ ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
███    █▀    ███    ███     ███    █▀  ███    █▀    ███▐██▀     ███    █▀    ███    ███ 
███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███         ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███        ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    █▄    ███    ███     ███    █▄  ███    █▄    ███▐██▄     ███    █▄  ▀███████████ 
███    ███   ███    ███     ███    ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
████████▀    ███    █▀      ██████████ ████████▀    ███   ▀█▀   ██████████   ███    ███ 
                                                    ▀                        ███    ███ 
    """))

tokenn = input(Colorate.Horizontal(Colors.red_to_green,' [>] path to .txt ->'))

for token in open((tokenn), 'r'):
    token = token.strip()
    if len(token) <= 50:
        print('Skipped ' + token)
        continue
    if token in checked:
        continue
    checked.append(token)

    userdata = json.loads(requests.get('https://discord.com/api/v9/users/@me', headers={'authorization': token}).text)
    if 'message' in userdata:
        print(Fore.RED + token + ' is invalid. ' + userdata['message'])
        invalid.append(token)
        continue

    if userdata['id'] in ids:
        print('Found user duplicate [' + userdata['id'] + ']')
        continue

    ids.append(userdata['id'])
    working.append(token)

    if userdata['verified']:
        verified.append(token)
    if userdata['phone']:
        phone.append(token)
    if 'premium_type' in userdata:
        if userdata['premium_type'] > 0:
            nitro.append(token)
    
    subscriptions = json.loads(requests.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers={'authorization': token}).text)
    if str(subscriptions).startswith('[') and len(subscriptions) > 0 and subscriptions[0]['payment_source_id']:
        billing.append(token)
    print(Fore.GREEN + token + ' is Valid.')

os.system("cls")

print(Colorate.Horizontal(Colors.red_to_green,str(len(working)) + ' Working Tokens'))

print(Colorate.Horizontal(Colors.red_to_green,str(len(verified)) + ' Verified Tokens'))

print(Colorate.Horizontal(Colors.red_to_green,str(len(phone)) + ' Phone Tokens'))

print(Colorate.Horizontal(Colors.red_to_green,str(len(billing)) + ' Billing Tokens'))

print(Colorate.Horizontal(Colors.red_to_green,str(len(nitro)) + ' Nitro Tokens'))

f = open('resultsTokens/working.txt', 'w')
f.write('\n'.join([str(e) for e in working]))
f.close()

f = open('resultsTokens/verified.txt', 'w')
f.write('\n'.join([str(e) for e in verified]))
f.close()

f = open('resultsTokens/phone.txt', 'w')
f.write('\n'.join([str(e) for e in phone]))
f.close()

f = open('resultsTokens/billing.txt', 'w')
f.write('\n'.join([str(e) for e in billing]))
f.close()

f = open('resultsTokens/nitro.txt', 'w')
f.write('\n'.join([str(e) for e in nitro]))
f.close()

f = open('resultsTokens/invalid.txt', 'w')
f.write('\n'.join([str(e) for e in invalid]))
f.close()

print(Colorate.Horizontal(Colors.red_to_green, """


    the results can be found here: DesmondTool/resultsTokens

    """))

os.system("pause")

os.system('cmd /k "python DesmondTool.py"')