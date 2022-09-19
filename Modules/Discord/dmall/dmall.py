import requests, time, os
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Desmond Tool | v1.0 | Developer: Zaphir")

UserChannelsAPI = "users/@me/channels"
SendMessageAPI = "v8/channels/{}/messages" 



class API:

    def __init__(self, Token:str):

        self.BASEURL = "https://discord.com/api/"
        self.headers = {'authorization' : Token}

        self.req = requests.session()

        self.ChannelIDs = []

        chan_req = requests.get(self.BASEURL+UserChannelsAPI, headers=self.headers)

        for x in list(chan_req.json()):
            self.ChannelIDs.append(x)

    def Message(self, content:str):

        data = {"content":content,"tts":False}
        
        for x in self.ChannelIDs:
            message_req = self.req.post(self.BASEURL+SendMessageAPI.format(x["id"]), headers=self.headers, json=data)
            
            if message_req.status_code == 429:
                time.sleep(10)
            elif message_req.status_code == 200:
                print("[$] Sent {}".format(str(x["id"])))
                


        
def Main():
    Token = input("[$] Enter Token -> ")
    
    Content = input("[$] Enter Content To Send -> ")

    print("-----")

    API(Token).Message(Content)

    os.system('cls')

    main()



if __name__ == "__main__":
    Main()

os.system("pause")

os.system('cmd /k "python DesmondTool.py"')