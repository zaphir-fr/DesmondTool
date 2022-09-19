from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import urllib.request
import os

qr = input(Colorate.Horizontal(Colors.red_to_green, '\n[>] Link or text ->'))

urllib.request.urlretrieve(f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={qr}",
f"{qr}.png")

print(Colorate.Horizontal(Colors.red_to_green, "download successful"))

os.system(f'cmd /k "{qr}.png"')

os.remove(f"{qr}.png")


os.system("pause >nul") 