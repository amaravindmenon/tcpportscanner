#TCP Port Scanner. This help to find all the open port in a given IP address

from socket import *
from sys import *
import re

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''


print("___________________________________________")
print("|  Scan for OPEN PORTS - By Aravind Menon |")
print("-------------------------------------------")
print("IN format : 0-255.0-255.0-255.0-255")
print("Automatically checks all the ports of given IP")
print(" ")


target = input("Enter the target IP Adddress: ")
#port = int(argv[2])

if(re.search(regex, target)):

    for i in range(0,65535):
            
        s = socket(AF_INET,SOCK_STREAM)

        try:
            s.connect((target,i))
            print("port %d is open" % i)
            open=i
            s.close()
        except:
            print("port %d is closed" % i)
            s.close()
    print(" ")
    print(" ")
    print("________________")
    print(" Scan Completed ")
    print("----------------")
    print("")
    print("Open Ports are: ")
    print(open)
    
else:
    print("Invalid IP address")

    
#Thankyou
#By Aravind Menon
