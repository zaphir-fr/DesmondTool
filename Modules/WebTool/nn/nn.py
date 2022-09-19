#!/usr/bin/env python
import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random

try:
    import requests
except ImportError:
    print('Error !! : Some dependencies are not installed')
    print('Error Occured!!!\nUse Non-Supported Version')
    input('Press Any Key To Use Non-supported Version')
    os.system('bash send.sh --sendsms')

# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']

# The Credit For This Code Goes To Panda Hackers https://github.com/HACK3RY2J/
# And The Contributors Mentioned At https://github.com/HACK3RY2J/ANon-SMS/
# If You Wanna Take Credits, Please Look Yourself Again!!

def clr():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def banner():
    clr()
    logo = """                                                  
                       _____
                   .d88888888bo.
                 .d8888888888888b.
                 8888888888888888b
                 888888888888888888
                 888888888888888888
                  Y8888888888888888
            ,od888888888888888888P
         .'`Y8P'```'Y8888888888P'
       .'_   `  _     'Y88888888b
      /  _`    _ `      Y88888888b   ____
   _  | /  \  /  \      8888888888.d888888b.
  d8b | | /|  | /|      8888888888d8888888888b
 8888_\ \_|/  \_|/      d888888888888888888888b
 .Y8P  `'-.            d88888888888888888888888
/          `          `      `Y8888888888888888     
|                        __    888888888888888P
 \                       / `   dPY8888888888P'
  '._                  .'     .'  `Y888888P`
     `"'-.,__    ___.-'    .-'
         `-._````  __..--'`           By Zaphir#0001
             ``````
                                         """
    print(logo)
    print("\n")
    

banner()


type = 0
try:
  if sys.argv[1] == "track":
    type = 1
except Exception:
  type = 0
if type == 1:
  print("Track The Anonymous Message You Sent Using This Tool.")
  print()
  Track()
elif type == 0:
  while True:
    print("Enter The Details Of The Person You Want To Send Anonymous Message")
    cc = input("\tEnter Country Code (Without +) : ")
    if '+' in cc:
            tc = list(cc)
            tc.remove('+')
            cc = ''.join(tc)
            cc = cc.strip()
    if len(cc) >= 4 or len(cc) < 1:
            print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
            continue
    pn = input("Enter Phone Number : +" + cc + " ")
    if len(pn) <= 6:
            print('\n\nInvalid Phone Number..\n')
            continue
    numbe = cc + pn
    if not numbe.isdigit():
                print('\n\nPhone Number Must Consist Of Numbers Only\n')
                continue
    receiver = '+' + numbe
    text = input("Enter Message to send : ")
    
    resp = requests.post('https://textbelt.com/text',{
      'phone' : receiver,
      'message' : text ,
      'key' : 'textbelt'
    })
    
    print(resp.json())
    time.sleep(9999)

