#!/usr/bin/python

import socket
import os

ip = "127.0.0.1"
port = 3540

data_connect = (ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(data_connect)

print("\x1b[1;32m" + "Conectado con el servidor ---> %s:%s" % (ip, port))


while True:
    try:
            # msg = raw_input("> ")
        client.send("respuesta")
        respuesta = client.recv(4096)
        # print(respuesta)
        if respuesta == 'ls':
            client.sendall(str(os.listdir('./')))
        
        if respuesta == "exit":
            break
    except KeyboardInterrupt:
        print("\x1b[1;31m" + "------- CONEXIoN CERRADA ---------")
        client.close()
