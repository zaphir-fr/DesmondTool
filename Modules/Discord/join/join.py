import requests
import ctypes
import os

ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")

token = input(' path to tokens.txt ->')
link = input('Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)

print (link)

with open((token),'r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("All valid tokens have joined!")

os.system("pause")

os.system('cmd /k "python DesmondTool.py"')