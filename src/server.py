import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '0.0.0.0'
port = 3000

server.bind(("", port))

server.listen(1)

while True:
    client, datos = server.accept()
    print "conectado" + str(datos)