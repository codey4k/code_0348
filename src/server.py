#!/usr/bin/python

import socket
import threading


ip = '0.0.0.0'
port = 3540
dataConection = (ip, port)
max_connect = 5

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(dataConection)

server.listen(max_connect)

print ("Esperando conecciones en %s : %s" % (ip, port) )

client, direction = server.accept()

print("Conexion establecida con %s:%s" % (direction[0], direction[1]))

while True:
    datos = client.recv(1024)
    print "conectado" + str(datos)
    print("RECIBIDO: %s" %datos)
    client.sendall("-- Recibido --")
    # server.send("-- Recibido --")