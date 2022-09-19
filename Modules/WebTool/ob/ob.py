from importlib.resources import contents
import os
import base64
from sys import argv
from genericpath import isfile
from traceback import print_tb
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System


def clear_console():
    os.system('cls')




# configuration
OFFSET = 10
VARIABLE_NAME = '__0x_zaphir' * 100

def obfuscate(content):

    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) + 1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += OFFSET
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code




def main():
   
    try:
        print("                                                                                                           ")
        
        path = input(Colorate.Horizontal(Colors.red_to_green, f"\n[>] Your File here "))
        print()
        if not isfile(path):
            input(Colorate.Horizontal(Colors.red_to_green, f"""doesn't exist!"""))
            exit()
        if not os.path.exists(path):
            print(Colorate.Horizontal(Colors.red_to_green, '[-] File not found'))
            exit()

        if not os.path.isfile(path) or not path.endswith('.py'):
            print(Colorate.Horizontal(Colors.red_to_green, '[-] Invalid file'))
            exit()
        
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()

        obfuscated_content = obfuscate(file_content)

        with open(f'{path.split(".")[0]} (obfuscated).py', 'w') as file:
            file.write(obfuscated_content)

        print(Colorate.Horizontal(Colors.red_to_green, '[+] Script has been obfuscated'))
    except:
        print(Colorate.Horizontal(Colors.red_to_green, f'Error : Check The Filename or FileLocation Properly'))

if __name__ == '__main__':
    main()


os.system("pause >nul") 