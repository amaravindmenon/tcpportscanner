#TCP Port Scanner. This help to find all the open port in a given IP address

from socket import *
from sys import *
import re
import threading

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

def scan(ab1,ab2):

    global psport

    if(re.search(regex, target)):

        for i in range(ab1,ab2):
            
            s = socket(AF_INET,SOCK_STREAM)

            try:
                s.connect((target,i))
                print("port %d is open" % i)
                open=i
                psport = open
                s.close()
            except:
                print("port %d is closed" % i)
                s.close()
    else:
        print("Invalid IP address")


t1 = threading.Thread(target=scan,args=(0,100))
t2 = threading.Thread(target=scan,args=(100,200))
t3 = threading.Thread(target=scan,args=(200,300))
t4 = threading.Thread(target=scan,args=(300,400))
t5 = threading.Thread(target=scan,args=(400,500))
t6 = threading.Thread(target=scan,args=(500,600))
t7 = threading.Thread(target=scan,args=(600,700))


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()


print(" ")
print(" ")
print("________________")
print(" Scan Completed ")
print("----------------")
print("")
print("Open Ports are: ")
print(psport)

    
#Thankyou
#By Aravind Menon
