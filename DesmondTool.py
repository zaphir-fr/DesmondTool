from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import sys,os
import webbrowser 
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")
os.system("cls")

def settings():
    print(Colorate.Horizontal(Colors.red_to_green, """
                      ██████  ███████ ███████ ███    ███  ██████  ███    ██ ██████  
                      ██   ██ ██      ██      ████  ████ ██    ██ ████   ██ ██   ██ 
                      ██   ██ █████   ███████ ██ ████ ██ ██    ██ ██ ██  ██ ██   ██ 
                      ██   ██ ██           ██ ██  ██  ██ ██    ██ ██  ██ ██ ██   ██ 
                      ██████  ███████ ███████ ██      ██  ██████  ██   ████ ██████                   (Beta 1.0)
    	""", 1))

    print(Colorate.Horizontal(Colors.red_to_green, """
                            1: Discord                      | 2: Webtool
                            3: About                      
                                                
    	""", 1))



banner = """

 ______________
|[]            |
|  __________  |
|  | Start  |  |
|  | Press  |  |
|  | Enter  |  |
|  |________|  |
|   ________   |
|   [ [ ]  ]   |
\___[_[_]__]___|
"""[1:]

Anime.Fade(Center.Center(banner), Colors.red_to_green, Colorate.Vertical, interval=0.025, enter=True)
settings()

command = input(Colorate.Horizontal(Colors.red_to_green, '\n[>] choose -> '))

if command == '1':
   os.system('cmd /k "python Modules//Discord///discord.py"')


if command == '2':
   os.system('cmd /k "python Modules//WebTool///WebTool.py"')


if command == '3':
   os.system("cls")
   print(Colorate.Horizontal(Colors.red_to_green, """
	
                     .                          
                     M                          
                    dM                          
                    MMr                         
                   4MMML                  .     
                   MMMMM.                xf     
   .              "MMMMM               .MM-     
    Mh..          +MMMMMM            .MMMM         
    .MMM.         .MMMMML.          MMMMMh      
     )MMMh.        MMMMMM         MMMMMMM       
      3MMMMx.     'MMMMMMf      xnMMMMMM"       
      '*MMMMM      MMMMMM.     nMMMMMMP"        
        *MMMMMx    "MMMMM\    .MMMMMMM=         
         *MMMMMh   "MMMMM"   JMMMMMMP           
           MMMMMM   3MMMM.  dMMMMMM            .
            MMMMMM  "MMMM  .MMMMM(        .nnMP"
=..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*  
  "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"   
   "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""     
     ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"        
        *PMMMMMMhn. *x > M  .MMMM**""           Zaphir#0001
           ""**MMMMhx/.h/ .=*"                  
                    .3P"%....                   
                  nP"     "*MMnx         

          Join Discord? (Yes or No)






""", 1))

zaph = input(Colorate.Horizontal(Colors.red_to_green, '\n[>] choose -> '))

if zaph == 'Yes':
	webbrowser.open('https://discord.gg/TDAG7xsGQF', new=2)
os.system('cmd /k "python DesmondTool.py"')

if zaph == 'No':
	print('Fuck YOu')
	time.sleep(1)
	os.system('cmd /k "python DesmondTool.py"')
	
if zaph == 'yes':
	webbrowser.open('https://discord.gg/q75ZSPMccv', new=2)
os.system('cmd /k "python DesmondTool.py"')

if zaph == 'no':
	print('Fuck YOu')
	time.sleep(1)
	os.system('cmd /k "python DesmondTool.py"')
	