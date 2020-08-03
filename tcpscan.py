from socket import *
from sys import *

target = argv[1]
#port = int(argv[2])

for i in range(0,5000):
    
    s = socket(AF_INET,SOCK_STREAM)

    
    try:
        s.connect((target,i))
        print("port %d is open" % i)
        s.close()
    except:
        print("port %d is closed" % i)
        s.close()
