#!/bin/python

import socket
import sys

if len(sys.argv) != 3:
  print ("Erro de sintaxe. Espera-se client-socket.py IP PORTA")
  exit()

# Instancia o socket
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  print ("Socket cliente criado com sucesso")
except socket.error as err:
  print ("Erro ao criar socket: %s" %(err))

# Recebe o IP e porta dos argumentos passados
host_ip = sys.argv[1]
port = int(sys.argv[2])

# Conecta com o socket servidor e printa a mensagem recebida
s.connect((host_ip, port))
print (s.recv(1024).decode())
