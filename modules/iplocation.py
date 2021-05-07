import requests
import os
import sys
import ipapi
from colorama import Fore,init
import time

def __start__():
    init()
    print(Fore.GREEN+"\n [+] "+Fore.WHITE+"Enter 'IP Address'")
    
    site = input(Fore.GREEN+" ┌─["+Fore.BLUE+"IGTOOLS"+"~"+Fore.RED+"@Root"+Fore.WHITE+"/"+"IP-Location"+Fore.GREEN+"""]
 └──╼ """+Fore.WHITE+"$ ")

    source = ipapi.location(ip=site)
    try:
        print (Fore.YELLOW+" [!]"+Fore.WHITE+" Please Wait While loading\n")
        time.sleep(5)
        print (Fore.GREEN+" [+]"+Fore.WHITE+" ip = "+ source["ip"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" version = "+ source["version"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" id country = "+source["country"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" country = "+ source["country_name"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" Calling Code = "+source["country_calling_code"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" country_code = "+ source["country_code"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" country_code_iso3 = "+ source["country_code_iso3"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" Languages = "+source["languages"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" city = " + source["city"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" region_code = "+ source["region_code"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" region = "+ source["region"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" org = "+ source["org"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" asn = "+ source["asn"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" currency_name = "+ source["currency_name"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" currency = "+ source["currency"])
        # print (Fore.GREEN+" [+]"+Fore.WHITE+" postal = "+ source["postal"])
        print (Fore.GREEN+" [+]"+Fore.WHITE+" utc_offset = "+ source["utc_offset"]+"\n")
        try:
            input(Fore.BLUE+" [$] "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()  
    except:
        print(Fore.RED+"Sorry Please Enter IP Address")
        sys.exit()



