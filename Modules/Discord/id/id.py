from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests
import json
import os 
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")

iid = input(Colorate.Horizontal(Colors.red_to_green,'\n[>] ID ->'))

os.system("cls")

r = requests.get(f"http://discord-pfp.herokuapp.com/api?id={iid}")



data = r.json()



username = data["username"]
discriminator = data["discriminator"]
public_flags = data["public_flags"]
id = data["id"]
avatar = data["avatar"]




print(Colorate.Horizontal(Colors.red_to_green, """
▒▒▒▒▒▒▒▒▒▒█▄▄▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒█▄░░░▀▒▒▒▒▒▒▒▒▒▒
▒▒▒▒█▄▀░░░▀▀▀█▒▒▒▒▒▒▒▒▒
▒█▄▀░░░░▀▀▀░░░▀█▒▒▒▒▒▒▒
▀░░░░▀▀▀░░░░░░░░▀▄▒▒▒▒▒
█░▀▀▀░░░░░░░░░░░░░▀▄▒▒▒
▒▄░░░░░░░░░░░░░░░░░░░▄▒
▒█░░░░░░░░░░███████▄██▒
▒▒▀░░░░░░░░░▒▒▒███▒▄▒▒▒
▒▒█░░░░░░░░░▒▒▒▒▒▒▒▄▒▒▒
▒▒▒▀▀▀▀▀▀▀▀▀▒▒▒▒▒▒▄█▒▒▒
▒▒▒█▄▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒
▒▒▒▒▄▒▒▒▒▒▒▒█▄█████▒▒▒▒
▒▒▒▒▒▄██▒▒▒█▄▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒███▄▒▒▒▒▒▒▒▒▒▒▒

	"""))





print(Colorate.Horizontal(Colors.red_to_green, " [1 Username:] : " + username))
print(Colorate.Horizontal(Colors.red_to_green, " [2 Discriminator:] : " + discriminator))
print(Colorate.Horizontal(Colors.red_to_green," [3 Public flags:] : " + str(public_flags)))
print(Colorate.Horizontal(Colors.red_to_green, " [4 Id:] : " + id))
print(Colorate.Horizontal(Colors.red_to_green, " [5 Avatar:] : " + avatar))

os.system("pause")

os.system('cmd /k "python DesmondTool.py"')