#!/bin/python

import socket

# Instancia o socket
try:
  s = socket.socket()
  print ("Socket servidor criado com sucesso")
except socket.error as err:
  print ("Erro ao criar socket: %s" %(err))

# Define a porta como 12345
port = 12345
s.bind(('', port))
print ("Porta %s" %(port))

# Habilita o socket para aceitar conexoes
# limite permitido antes de bloquear novas conexoes = 5
s.listen(5)
print ("Aguardando conexao")

# Loop infinito que recebe conexoes e manda uma string para o cliente
while True:
  c, addr = s.accept()
  print ('Conexao recebida de: ', addr )
  c.send('Socket servidor: conexao estabelecida com sucesso'.encode())
  c.close()
