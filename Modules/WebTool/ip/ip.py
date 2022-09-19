from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests
import json
import os 

ip = input(Colorate.Horizontal(Colors.red_to_green, " [>] IP ADDRESS : ")); ip.replace(" ", "")


r = requests.get(f"http://ip-api.com/json/{ip}")
r2 = requests.get(f"https://ipinfo.io/{ip}")
values = json.loads(r.text)
data = r2.json()
city = data["city"]
location = data["loc"].split(",")
latitude = location[0]
longitude = location[1]

print(Colorate.Horizontal(Colors.red_to_green, "\n [1] : " + values["country"] + f" [{values['countryCode']}]"))
print(Colorate.Horizontal(Colors.red_to_green, " [2] : " + values["regionName"] + f" [{values['region']}]"))
print(Colorate.Horizontal(Colors.red_to_green, " [3] : " + city))
print(Colorate.Horizontal(Colors.red_to_green, " [4] : " + values["timezone"]))
print(Colorate.Horizontal(Colors.red_to_green, " [5] : " + values["isp"]))

os.system("pause >nul") 