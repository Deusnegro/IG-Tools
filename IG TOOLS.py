import os
import sys
from colorama import Fore,init
import time 
import socket
from helplist import helpp
from modules import cms,Traceroute,reverseip,portscan,iplocation,httpheader,findsharedns,whois,dnslookup,robots,finder,cloudflare,wordpress



try:
    from colorama import Fore
except:
    os.system("cls")
    print(Fore.YELLOW+"[!]"+Fore.WHITE+"Please Install colorama Enter CMD:('pip install colorama')")

#---------------------------

try:
    import requests
except:
    os.system("cls")
    print(Fore.YELLOW+"[!]"+Fore.WHITE+"Please Install requests Enter CMD:('pip install requests')")

#---------------------------


try:
    import ipapi
except:
    os.system("cls")
    print(Fore.YELLOW+"[!]"+Fore.WHITE+"Please Install ipapi Enter CMD:('pip install ipapi')")

#---------------------------

try:
    import builtwith
except:
    os.system("cls")
    print(Fore.YELLOW+"[!]"+Fore.WHITE+"Please Install builtwith Enter CMD:('pip install builtwith')")

    #--------------------------

while True:
 try:    
    helpp.Banner()
    helpp.infolist1()
    inp = input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+Fore.BLUE+"~"+Fore.RED+"@Root"+Fore.GREEN+"""]
 └──╼ """+Fore.WHITE+"$ ")
    if inp == "-k":
        helpp.infolist2()
    elif inp == "-h":
        helpp.infohelp()
    elif inp == "-q":
        helpp.infowp()
        owp=input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+Fore.BLUE+"~"+Fore.RED+"@Root"+Fore.WHITE+"/"+"CMS Detection"+Fore.GREEN+"""]
 └──╼ """+Fore.WHITE+"$ ")
        if owp == "-p":
            helpp.Banner()
            wordpress.wpplug()
        elif owp == "-U":
            helpp.Banner()
            wordpress.user()
        elif owp == "-M":
            try:
                input(Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
            except:
                print("\n")
                sys.exit()
    elif inp == "-B":
        helpp.Banner()
        cloudflare.__start__()
    elif inp == "-c":
        helpp.Banner()
        cms.__start__()
    elif inp == "-T":
        helpp.Banner()
        Traceroute.__start__()
    elif inp == "-V":
        helpp.Banner()
        reverseip.__start__()
    elif inp == "-P":
        helpp.Banner()
        portscan.__start__()
    elif inp == "-H":
        helpp.Banner()
        httpheader.__start__()
    elif inp == "-D":
        helpp.Banner()
        findsharedns.__start__()
    elif inp == "-W":
        helpp.Banner()
        whois.__start__()
    elif inp == "-L":
        helpp.Banner()
        dnslookup.__start__()
    elif inp == "-R":
        helpp.Banner()
        robots.__start__()
    elif inp == "-F":
        helpp.Banner() 
        finder.__start__()
    elif inp == "-i":
        helpp.Banner()
        iplocation.__start__()
    elif inp == "-X":
        helpp.Banner()
        print(Fore.RED+"GOOD BAY ;)")
        sys.exit()
    elif inp == "":
        sys.exit()
        print(Fore.YELLOW+"  [!]  "+Fore.WHITE+"Error: data nat faund")

    # elif inf == "-G":
    #     helpp.Banner()
    #     listdirectory.__start__()

    #Next Update in Ig tools (;
    #ListDirectory
 except KeyboardInterrupt:
       print("")
       sys.exit()      



