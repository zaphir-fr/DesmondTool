from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests, os, time, ctypes

def clear():
    if os.name != 'nt':
        os.system('clear')
    else:
        os.system('cls')

def ititle(si, fi, r):
    try:
        ctypes.windll.kernel32.SetConsoleTitleW('Sent [{0}] | Failed [{1}] | Rate Limited [{2}]'.format(si, fi, r))
    except:
        pass

def whsend(hook: str, name: str, content: str, s: bool):
    clear()
    if s:
        sent = 0
        failed = 0
        rl = 0
        while failed < 20:
            r = requests.post(hook, { "content": content, "username": name })
            try:
                if r.json()["retry_after"]:
                    print(f'Getting rate limited, sleeping for {r.json()["retry_after"] / 1000}s.')
                    rl += 1
                    ititle(sent, failed, rl)
                    time.sleep(r.json()["retry_after"] / 1000)
            except:
                if r.status_code == 204:
                    sent += 1
                    ititle(sent, failed, rl)
                    print(f'Successful | {sent} times.')
                else:
                    failed += 1
                    ititle(sent, failed, rl)
                    print(f'Failed | {failed} times.')
        clear()
        exit(f'The webhook most likely does not exist anymore.\nStatistics:\nSuccessful posts: {sent}\nFailed posts: {failed}\nRate Limits: {rl}')
    else:
        r = requests.post(hook, { "content": content, "username": name })
        if r.status_code == 204:
            print(Colorate.Horizontal(Colors.blue_to_purple, '  Successful.'))
        else:
            print(Colorate.Horizontal(Colors.blue_to_purple, '  Failed.'))


url = input(Colorate.Horizontal(Colors.blue_to_purple, '  Webhook URL: '))
if not url:
    print(Colorate.Horizontal(Colors.blue_to_purple, '  you must enter a webhook URL.'))
    exit(-1)
un = input(Colorate.Horizontal(Colors.blue_to_purple, '  Username Override (optional): '))
if not un:
    un = 'appendable'
c = input(Colorate.Horizontal(Colors.blue_to_purple, '  Content to send: '))
if not c:
    print(Colorate.Horizontal(Colors.blue_to_purple, '  you must enter content to send.'))
    exit(-1)
sp = input(Colorate.Horizontal(Colors.blue_to_purple, '  Spam? [y|n]: '))
if not sp:
    whsend(url, un, c, True)
if sp.lower() == 'y':
    whsend(url, un, c, True)
else:
    whsend(url, un, c, False)