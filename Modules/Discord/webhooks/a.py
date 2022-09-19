from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import time
import os
from colorama import Fore, init
import requests
import requests

init()
banner = (Fore.MAGENTA + """




    """ + Fore.LIGHTCYAN_EX)
print(banner)
webhook = input(Colorate.Horizontal(Colors.blue_to_purple, " [INPUT] ENTER THE WEBHOOK TO DELETE : "))

def delete():
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print(Colorate.Horizontal(Colors.blue_to_purple, "\n [LOGS] WEBHOOK SUCCESFULLY DELETED"))
        os.system("pause >nul")  # Pause command in Batch (press any key to exit the code)
    elif check.status_code == 200:
        print(Colorate.Horizontal(Colors.blue_to_purple, "\n [LOGS] FAILED TO DELETE WEBHOOK"))
        os.system("pause >nul")

test = requests.get(webhook)
if test.status_code == 404:
    print(Colorate.Horizontal(Colors.blue_to_purple, "\n [LOGS] THE WEBHOOK IS INVALID"))
    os.system("pause >nul")
elif test.status_code == 200:
    print(Colorate.Horizontal(Colors.blue_to_purple, "\n [LOGS] THE WEBHOOK IS VALID"))
    delete()