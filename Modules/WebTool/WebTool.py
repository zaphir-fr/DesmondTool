from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import sys,os
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")
os.system("cls")

def settings():
    print(Colorate.Horizontal(Colors.red_to_green, """


      ██╗    ██╗███████╗██████╗ ████████╗ ██████╗  ██████╗ ██╗ 
      ██║    ██║██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     
      ██║ █╗ ██║█████╗  ██████╔╝   ██║   ██║   ██║██║   ██║██║     
      ██║███╗██║██╔══╝  ██╔══██╗   ██║   ██║   ██║██║   ██║██║     
      ╚███╔███╔╝███████╗██████╔╝   ██║   ╚██████╔╝╚██████╔╝███████╗
       ╚══╝╚══╝ ╚══════╝╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                             

    	""", 1))

    print(Colorate.Horizontal(Colors.red_to_green, """
      1: ProxyScrape                          | 2: Spoof SMS ( 1sms = 1day) 
      3: Obfuscation Python                   | 4. Creator QR Code
      5: IP lookup                            
    	



      """, 1))


settings()
command = input(Colorate.Horizontal(Colors.red_to_green, '\n[>] choose -> '))


if command == '1':
   os.system('cmd /k "python Modules//WebTool///proxy////proxy.py"')

if command == '2':
   os.system('cmd /k "python Modules//WebTool///nn////nn.py"')

if command == '3':
   os.system('cmd /k "python Modules//WebTool///ob////ob.py"')

if command == '4':
   os.system('cmd /k "python Modules//WebTool///qr////qr.py"')

if command == '5':
   os.system('cmd /k "python Modules//WebTool///ip////ip.py"')

if command == '6':
   print('soon...')