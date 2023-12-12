
from pickle import TRUE
import re

def GoodOrBadipv4(ip_address):
    pattern = r'^((([01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.){3}([01]?[0-9]{1,2}|2[0-4][0-9]|25[0-5]))$'
    if re.match(pattern, ip_address):
        return True
    else:
        return False
while (TRUE):
    ip = input("What is IP? \n(If you vanna close type 'close') \n ")
    if ip=="close":
        print("OK")
        break
    if GoodOrBadipv4(ip):
        print(ip, "is good IP \n \n")
    else:
        print(ip, "is bad IP \n \n")