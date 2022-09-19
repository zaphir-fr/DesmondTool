import requests
import six
from lxml import html
from threading import Thread
from queue import Queue
import os

os.system("cls")

class Worker(Thread):


    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as ex:
                pass
            finally:
                self.tasks.task_done()


class ThreadPool:

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):

     self.tasks.put((func, args, kargs))

    def map(self, func, args_list):

        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):

        self.tasks.join()


filename = 'DesmondProxys.txt'
'''
def removedupes(inputfile, outputfile):
    lines = open(inputfile, 'r').readlines()
    lines_set = set(lines)
    out = open(outputfile, 'w')
    for line in lines_set:
        out.write(line)
    print('\nScan completed.\nRemoved any/all dupes.')
'''


def scrapesocks():
    src = requests.get('https://www.socks-proxy.net/')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",", "")
        link = link.replace("Yes", "") and link.replace("[", "") and link.replace("]", "")
        if not ' ' in link:
            print(link)
            with open(filename, 'a') as handle:
                handle.write(link + '\n')
                handle.close()


def scrapeus():
    src = requests.get('https://www.us-proxy.org/')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",", "")
        link = link.replace("no", "")
        link = link.replace("[", "")
        link = link.replace("]", "")
        if not ' ' in link:
            print(link)
            with open(filename, 'a') as handle:
                handle.write(link + '\n')
                handle.close()


def scrapefree():
    src = requests.get('https://free-proxy-list.net/')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",","")
        link = link.replace("no","") and link.replace("[","") and \
link.replace("]","")
        if not ' ' in link:
            print(link)
            with open(filename,'a') as handle:
                handle.write(link + '\n')
                handle.close()


def scrapeuk():
    src = requests.get('https://free-proxy-list.net/uk-proxy.html')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",", "")
        link = link.replace("no", "") and link.replace("[", "") and \
link.replace("]", "")
        if not ' ' in link:
            print(link)
            with open(filename, 'a') as handle:
                handle.write(link + '\n')
                handle.close()


def scrapeanon():
    src = requests.get('https://free-proxy-list.net/anonymous-proxy.html')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",", "")
        link = link.replace("yes", "") and link.replace("[", "") and   \
link.replace("]", "") and link.replace("no",
                                                                                                                "")
        if not ' ' in link:
            print(link)
            with open(filename, 'a') as handle:
                handle.write(link + '\n')
                handle.close()


def scrapessl():
    src = requests.get('https://www.sslproxies.org/')
    tree = html.fromstring(src.content)
    td = tree.xpath('//td/text()')
    a = str(td)
    b = a.split("'")
    links = b
    for link in links:
        link = link.split('"')[0].replace(",", "")
        link = link.replace("yes", "") and link.replace("[", "") and link.replace("]", "") and \
link.replace("no",
                                                                                                                "")
        if not ' ' in link:
            print(link)
            with open(filename, 'a') as handle:
                handle.write(link + '\n')
                handle.close()





def main():



    print(
            "Choose proxies to scrape\n   [1] FREE\n   [2] US\n   [3] UK\n   [4] SOCKS\n   [5] ANONYMOUS\n   [6] SSL\n   [0] ALL TYPES")

    Choice = int(input("Selection = "))

    print("Now Scraping")
    
    if Choice == 1:
        pool = ThreadPool(200)
        pool.add_task(scrapefree)
        pool.wait_completion()

    if Choice == 2:
        pool = ThreadPool(200)
        pool.add_task(scrapeus)
        pool.wait_completion()

    if Choice == 3:
        pool = ThreadPool(200)
        pool.add_task(scrapeuk)
        pool.wait_completion()

    if Choice == 4:
        pool = ThreadPool(200)
        pool.add_task(scrapesocks)
        pool.wait_completion()

    if Choice == 5:
        pool = ThreadPool(200)
        pool.add_task(scrapeanon)
        pool.wait_completion()

    if Choice == 6:
        pool = ThreadPool(200)
        pool.add_task(scrapessl)
        pool.wait_completion()

    if Choice == 0:
        pool = ThreadPool(200)
        pool.add_task(scrapesocks)
        pool.wait_completion()
        pool.add_task(scrapeus)
        pool.wait_completion()
        pool.add_task(scrapeuk)
        pool.wait_completion()
        pool.add_task(scrapeanon)
        pool.wait_completion()
        pool.add_task(scrapefree)
        pool.wait_completion()
        pool.add_task(scrapessl)
        pool.wait_completion()

    print("Done!")
    os.system('cmd /k "DesmondProxys.txt"')
    os.remove("DesmondProxys.txt")


'''
def Clear():
    list = ["Free", "US", "UK", "Socks", "Anonymous", "SSL" "Brazil", "Czech",
                                            "Finland", "France", "Canada", "Germany", "Hungary", "Italy", "Netherlands",
                                            "Norway", "Poland", "Russia", "Spain", "Sweden", "Switzerland", "Bangladesh", "Australia", "India", "Japan", "Singapore"
                                            "KH", "IT", "TH", "BR", "CO", "US", "UA", "PL", "RU", "IN", "NO", "BD", "ZA", "LV", "MY", "ID", "EC", "BY", 
                                            "RS", "CR", "AR", "SI", "PS" 
                                    ]
    with open("DesmondProxys.txt", "r") as f:
        lines = f.readlines()
        with open("DesmondProxys.txt", "w") as f:
            for line in list:
                if line.strip("\n") == list:
                    f.write(line)
'''

if __name__ == '__main__':
    main()
    #Clear()