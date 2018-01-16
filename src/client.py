#!/usr/bin/python

import socket

ip = "127.0.0.1"
port = 3540

dataConect = (ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(dataConect)

print("Conectado con el servidor ---> %s:%s" % (ip, port))


while True:
    msg = raw_input("> ")
    client.send(msg)
    respuesta = client.recv(4096)
    print(respuesta)
    if respuesta == "exit":
        break;

print("------- CONEXIoN CERRADA ---------")
client.close()
