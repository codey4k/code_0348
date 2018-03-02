#!/usr/bin/python

import socket
import threading

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        
    def mount(self):
        data_conection = (self.ip, self.port)
        max_connect = 5
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(data_conection)
        server.listen(max_connect)
        print ("Esperando conecciones en %s : %s" % (self.ip, self.port) )
        client, direction = server.accept()
        print("Conexion establecida con %s:%s" % (direction[0], direction[1]))

        while True:
            data = client.recv(1024)
            print "conectado" + str(datos)
            print("RECIBIDO: %s" % data)
            client.sendall("-- Recibido --")
            # server.send("-- Recibido --")

def main():
    server = Server("0.0.0.0", 3540)
    
    
if __name__ == "__main__":
    main()
    