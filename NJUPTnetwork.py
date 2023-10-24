from inc.api import *
import sys
import time

username = sys.argv[1]
password = sys.argv[2]
while True:
    # try:
    #     ip = getIP()
    #     if checkIP(ip) == False:
    #        login(username, password)
    # except:
    #     pass
    print("login excuting....")
    if checkNetworked():
        print("Internet has been always networked")
    else :
        login(username, password)
        print("login executed.")

    time.sleep(5)
